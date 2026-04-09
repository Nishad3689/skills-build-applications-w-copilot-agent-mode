import logo from './octofitapp-small.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="OctoFit Logo" />
        <h1 style={{margin: 0, fontWeight: 700, fontSize: '2.2rem'}}>OctoFit Tracker</h1>
      </header>
      <nav>
        <a href="/">Home</a>
        <a href="/activities">Activities</a>
        <a href="/teams">Teams</a>
        <a href="/leaderboard">Leaderboard</a>
        <a href="/workouts">Workouts</a>
      </nav>
      <main style={{padding: '2rem'}}>
        <h2>Welcome to OctoFit Tracker!</h2>
        <p>Track your fitness activities, join teams, and compete on the leaderboard.</p>
        <button>Get Started</button>
      </main>
    </div>
  );
}

export default App;
