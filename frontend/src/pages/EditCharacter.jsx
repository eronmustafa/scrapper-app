import { useState, useEffect } from 'react';
import { useParams, useSearchParams, useNavigate } from 'react-router-dom';
import axios from 'axios'; // Import Axios
import { toast, ToastContainer } from 'react-toastify'; // Import Toastify
import 'react-toastify/dist/ReactToastify.css'; // Import Toastify styles
import '../EditCharacter.css'; // Import your custom CSS

export const EditCharacter = () => {
  const { id } = useParams();
  const [searchParams] = useSearchParams();
  const tableName = searchParams.get('table');
  const [character, setCharacter] = useState({
    character_name: '',
    actor_name: '',
    description: '',
    image_url: ''
  });
  const navigate = useNavigate();

  useEffect(() => {
    fetchCharacter();
  }, []);

  const fetchCharacter = async () => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:5000/characters/${id}`,
        {
          params: { table: tableName } // Pass query params using Axios
        }
      );
      setCharacter(response.data);
    } catch (error) {
      console.error('Error fetching character:', error);
      toast.error('Failed to load character data.');
    }
  };

  const handleChange = (e) => {
    setCharacter({ ...character, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.put(
        `http://127.0.0.1:5000/characters/${id}`,
        character,
        {
          params: { table: tableName }, // Pass query params
          headers: { 'Content-Type': 'application/json' }
        }
      );
      if (response.status === 200) {
        toast.success('Character updated successfully!'); // Show success toast
        navigate(`/characters?table=${tableName}`);
      }
    } catch (error) {
      console.error('Error updating character:', error);
      toast.error('Failed to update character. Please try again.');
    }
  };

  return (
    <div className="edit-character-container">
      <form className="edit-character-form" onSubmit={handleSubmit}>
        <h2>Edit Character</h2>
        <label className="form-label">
          Name:
          <input
            name="character_name"
            value={character.character_name}
            onChange={handleChange}
            className="form-input"
            required
          />
        </label>
        <label className="form-label">
          Actor:
          <input
            name="actor_name"
            value={character.actor_name}
            onChange={handleChange}
            className="form-input"
            required
          />
        </label>
        <label className="form-label">
          Description:
          <textarea
            name="description"
            value={character.description}
            onChange={handleChange}
            className="form-textarea"
            required
          />
        </label>
        <label className="form-label">
          Image URL:
          <input
            name="image_url"
            value={character.image_url}
            onChange={handleChange}
            className="form-input"
            required
          />
        </label>
        <button type="submit" className="submit-button">
          Save
        </button>
      </form>
      <ToastContainer /> {/* Add Toastify container */}
    </div>
  );
};

export default EditCharacter;
