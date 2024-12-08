from flask import Blueprint, jsonify, request, current_app
import asyncpg

characters_bp = Blueprint('characters', __name__)

# Fetch all characters
@characters_bp.route('/characters', methods=['GET'])
async def get_characters():
    pool = current_app.config['DB_POOL']
    table = request.args.get('table', 'vikings_characters')
    search = request.args.get('search', '')

    if table not in ['vikings_characters', 'norsemen_characters']:
        return jsonify({"error": "Invalid table name"}), 400

    query = f"""
        SELECT * FROM {table}
        WHERE character_name ILIKE $1 OR actor_name ILIKE $1 OR description ILIKE $1;
    """
    async with pool.acquire() as conn:
        try:
            results = await conn.fetch(query, f"%{search}%")
        except asyncpg.exceptions.PostgresError as e:
            return jsonify({"error": str(e)}), 500

    return jsonify([dict(record) for record in results])

# Fetch a specific character by ID
@characters_bp.route('/characters/<int:character_id>', methods=['GET'])
async def get_character(character_id):
    pool = current_app.config['DB_POOL']
    table = request.args.get('table', 'vikings_characters')

    if table not in ['vikings_characters', 'norsemen_characters']:
        return jsonify({"error": "Invalid table name"}), 400

    query = f"SELECT * FROM {table} WHERE id = $1;"
    async with pool.acquire() as conn:
        try:
            record = await conn.fetchrow(query, character_id)
        except asyncpg.exceptions.PostgresError as e:
            return jsonify({"error": str(e)}), 500

    if not record:
        return jsonify({"error": "Character not found"}), 404

    return jsonify(dict(record))

# Update a character by ID
@characters_bp.route('/characters/<int:character_id>', methods=['PUT'])
async def update_character(character_id):
    pool = current_app.config['DB_POOL']
    table = request.args.get('table', 'vikings_characters')

    if table not in ['vikings_characters', 'norsemen_characters']:
        return jsonify({"error": "Invalid table name"}), 400

    data = request.json
    character_name = data.get('character_name')
    actor_name = data.get('actor_name')
    description = data.get('description')
    image_url = data.get('image_url')

    if not all([character_name, actor_name, description, image_url]):
        return jsonify({"error": "All fields are required"}), 400

    query = f"""
        UPDATE {table}
        SET character_name = $1, actor_name = $2, description = $3, image_url = $4
        WHERE id = $5
        RETURNING *;
    """
    async with pool.acquire() as conn:
        try:
            updated_record = await conn.fetchrow(
                query, character_name, actor_name, description, image_url, character_id
            )
        except asyncpg.exceptions.PostgresError as e:
            return jsonify({"error": str(e)}), 500

    if not updated_record:
        return jsonify({"error": "Character not found or update failed"}), 404

    return jsonify(dict(updated_record)), 200
