import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Characters from './pages/Characters';
import CharacterDetails from './components/CharacterDetails';
import EditCharacter from './pages/EditCharacter';
import './App.css'; // Import custom styles

const App = () => (
  <div className="app-container">
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/characters" element={<Characters />} />
        <Route path="/character/:id" element={<CharacterDetails />} />
        <Route path="/character/edit/:id" element={<EditCharacter />} />
      </Routes>
    </Router>
  </div>
);

export default App;
