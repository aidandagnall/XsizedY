import logo from '../logo.svg';
import './App.css';
import React from 'react';
import Pair from '../components/Pair';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1> Would you rather fight...</h1>
        <div className="Choices">
          <Pair />
        </div>
      </header>

    </div>
  );
}

export default App;
