import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import PropTypes from 'prop-types';
import axios from 'axios';
import './../CharacterTable.css';

const CharacterTable = ({ tableName }) => {
  const [characters, setCharacters] = useState([]);
  const [search, setSearch] = useState('');
  const navigate = useNavigate();

  const API_URL = import.meta.env.VITE_API_URL;

  useEffect(() => {
    fetchCharacters();
  }, [search, tableName]);

  const fetchCharacters = async () => {
    try {
      const response = await axios.get(`${API_URL}/characters`, {
        params: { table: tableName, search },
      });
      console.log('API Response:', response.data); // Debug API response
      setCharacters(Array.isArray(response.data) ? response.data : []); // Ensure array
    } catch (error) {
      console.error('Failed to fetch characters:', error);
      setCharacters([]); // Fallback to an empty array on error
    }
  };

  return (
    <div className="character-table-container">
      <h2>{tableName === 'vikings_characters' ? 'Vikings Characters' : 'Norsemen Characters'}</h2>
      <input
        type="text"
        placeholder="Search characters..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="search-bar"
      />
      <div className="table-wrapper">
        <table className="styled-table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Actor</th>
              <th>Description</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {Array.isArray(characters) &&
              characters.map((char) => (
                <tr key={char.id}>
                  <td>{char.character_name}</td>
                  <td>{char.actor_name}</td>
                  <td>{char.description}</td>
                  <td className="action-buttons">
                    <button
                      className="details-button"
                      onClick={() => navigate(`/character/${char.id}?table=${tableName}`)}
                    >
                      Details
                    </button>
                    <button
                      className="edit-button"
                      onClick={() => navigate(`/character/edit/${char.id}?table=${tableName}`)}
                    >
                      Edit
                    </button>
                  </td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

CharacterTable.propTypes = {
  tableName: PropTypes.string.isRequired,
};

export default CharacterTable;
