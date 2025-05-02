import React, { useState, useEffect } from 'react';

function App() {
  const [searchTerm, setSearchTerm] = useState('');
  const [dbFilter, setDbFilter] = useState(['st', 'sp']);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const searchMedia = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ keyword: searchTerm, db_filter: dbFilter })
      });
      const data = await response.json();
      setResults(data.results);
    } catch (error) {
      console.error('Search error:', error);
    } finally {
      setLoading(false);
    }
  };

  const toggleDbFilter = (db) => {
    setDbFilter(prev => 
      prev.includes(db) ? prev.filter(d => d !== db) : [...prev, db]
    );
  };

  useEffect(() => { searchMedia(); }, []);

  return (
    <div className="app-container">
      <h1>IMAGO Media Search</h1>
      
      <div className="search-controls">
        <input
          type="text"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Search media..."
          onKeyPress={(e) => e.key === 'Enter' && searchMedia()}
        />
        <button onClick={searchMedia}>Search</button>
      </div>

      <div className="filter-controls">
        <label>
          <input 
            type="checkbox" 
            checked={dbFilter.includes('stock')} 
            onChange={() => toggleDbFilter('stock')} 
          /> Stock (ST)
        </label>
        <label>
          <input 
            type="checkbox" 
            checked={dbFilter.includes('sport')} 
            onChange={() => toggleDbFilter('sport')} 
          /> Sport (SP)
        </label>
      </div>

      {loading ? (
        <div className="loading">Loading...</div>
      ) : (
        <div className="results-grid">
          {results.map((item) => (
            <div key={item.media_id} className="media-card">
              <img 
                src={`http://localhost:8000${item.thumbnail_url}`}
                alt={item.title || 'Media image'}
                onError={(e) => e.target.src = 'placeholder.jpg'}
              />
              <h3>{item.title || 'Untitled'}</h3>
              <p>: {item.description}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;