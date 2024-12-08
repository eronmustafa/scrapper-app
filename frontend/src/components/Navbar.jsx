
import { Link } from 'react-router-dom';
import '../Navbar.css'; // Import the CSS for styling

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-content">
        <Link to="/" className="navbar-link">
          Home
        </Link>
        <Link to="/characters?table=vikings_characters" className="navbar-link">
          Table Characters (Vikings & Norsemen)
        </Link>
        {/* <Link to="/characters?table=norsemen_characters" className="navbar-link">
          Norsemen
        </Link> */}
      </div>
    </nav>
  );
};

export default Navbar;
