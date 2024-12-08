
import '../Home.css';

const Home = () => {
    return (
      <div className="home-container">
        <header className="home-header">
          <h1>Welcome to the Character Database</h1>
          <p>Explore detailed information about your favorite characters from Vikings and Norsemen!</p>
        </header>
        <section className="home-stats">
          <div className="stat-card">
            <h2>Vikings Characters</h2>
            <p>Discover 50+ characters from the Viking saga.</p>
          </div>
          <div className="stat-card">
            <h2>Norsemen Characters</h2>
            <p>Meet 30+ characters from the Norsemen series.</p>
          </div>
          <div className="stat-card">
            <h2>Dynamic and Editable</h2>
            <p>Edit character information and explore details at any time.</p>
          </div>
        </section>
      </div>
    );
  };

export default Home;
