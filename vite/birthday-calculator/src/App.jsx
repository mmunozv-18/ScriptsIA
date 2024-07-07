// src/App.jsx

import React from 'react';
import DateDifferenceCalculator from './components/DateDifferenceCalculator';
import './App.css';

const App = () => {
  return (
    <div className="App">
      <h1>Calculadora de diferencia entre fechas de nacimiento</h1>
      <DateDifferenceCalculator />
    </div>
  );
};

export default App;