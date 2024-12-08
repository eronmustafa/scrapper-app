import CharacterTable from '../components/CharacterTable';

const Characters = () => (
  <div>
    <h1>Characters</h1>
    <CharacterTable tableName="vikings_characters" />
    <CharacterTable tableName="norsemen_characters" />
  </div>
);

export default Characters;
