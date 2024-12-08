import { useEffect, useState } from 'react';
import { useParams, useSearchParams } from 'react-router-dom';
import axios from 'axios';
import '../CharacterDetails.css';

const CharacterDetails = () => {
  const { id } = useParams();
  const [searchParams] = useSearchParams();
  const tableName = searchParams.get('table');
  const [character, setCharacter] = useState(null);

  const API_URL = import.meta.env.VITE_API_URL;

  useEffect(() => {
    fetchCharacter();
  }, []);

  const fetchCharacter = async () => {
    try {
      const response = await axios.get(`${API_URL}/characters/${id}`, {
        params: { table: tableName }, // Pass query params using Axios
      });
      setCharacter(response.data);
    } catch (error) {
      console.error('Error fetching character details:', error);
      alert('Failed to load character details.');
    }
  };

  if (!character) return <div className="loading">Loading...</div>;

  return (
    <div className="character-details-container">
      <div className="character-details-card">
        <h2>Character Details</h2>
        <div className="character-info">
          <p><strong>Name:</strong> {character.character_name}</p>
          <p><strong>Actor:</strong> {character.actor_name}</p>
          <p><strong>Description:</strong> {character.description}</p>
        </div>
        {character.image_url && (
          <img
            className="character-image"
            src={character.image_url}
            alt={character.character_name}
          />
        )}
      </div>
    </div>
  );
};

export default CharacterDetails;
