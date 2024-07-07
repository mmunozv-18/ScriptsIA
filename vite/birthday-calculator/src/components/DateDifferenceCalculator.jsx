// src/components/DateDifferenceCalculator.jsx

import React, { useState } from 'react';
import './DateDifferenceCalculator.css';

const DateDifferenceCalculator = () => {
  const [date1, setDate1] = useState('');
  const [date2, setDate2] = useState('');
  const [difference, setDifference] = useState(null);

  const calculateDifference = () => {
    const firstDate = new Date(date1);
    const secondDate = new Date(date2);
    const diffTime = Math.abs(secondDate - firstDate);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    setDifference(diffDays);
  };

  return (
    <div className="calculator-container">
      <div className="input-container">
        <label htmlFor="date1">Fecha de Nacimiento 1:</label>
        <input
          type="date"
          id="date1"
          value={date1}
          onChange={(e) => setDate1(e.target.value)}
        />
      </div>
      <div className="input-container">
        <label htmlFor="date2">Fecha de Nacimiento 2:</label>
        <input
          type="date"
          id="date2"
          value={date2}
          onChange={(e) => setDate2(e.target.value)}
        />
      </div>
      <button onClick={calculateDifference} className="calculate-button">
        Calcular Diferencia
      </button>
      {difference !== null && (
        <p className="result">
          La diferencia entre las dos fechas es de {difference} días.
        </p>
      )}
    </div>
  );
};

export default DateDifferenceCalculator;