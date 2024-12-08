import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import PropTypes from 'prop-types'; // Import PropTypes for validation
import axios from 'axios'; // Import Axios
import './../CharacterTable.css'; // Import custom styles

const CharacterTable = ({ tableName }) => {
  const [characters, setCharacters] = useState([]);
  const [search, setSearch] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    fetchCharacters();
  }, [search, tableName]);

  const fetchCharacters = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/characters', {
        params: { table: tableName, search }, // Pass query parameters using Axios
      });
      setCharacters(response.data);
    } catch (error) {
      console.error('Failed to fetch characters:', error);
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
            {characters.map((char) => (
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

// Add PropTypes for type validation
CharacterTable.propTypes = {
  tableName: PropTypes.string.isRequired, // tableName must be a string and is required
};

export default CharacterTable;
