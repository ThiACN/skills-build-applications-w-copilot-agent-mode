import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespaceName
    ? `https://${codespaceName}-8000.app.github.dev/api/leaderboard/`
    : 'http://localhost:8000/api/leaderboard/';

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Leaderboard endpoint:', endpoint);
        console.log('Fetched leaderboard:', data);
        setLeaderboard(data.results ? data.results : data);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [endpoint]);

  return (
    <div>
      <h2 className="mb-4 text-success">Leaderboard</h2>
      <div className="card shadow-sm mb-4">
        <div className="card-body">
          <table className="table table-striped table-bordered">
            <thead className="table-success">
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Score</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.length === 0 ? (
                <tr><td colSpan="3" className="text-center">No leaderboard data found.</td></tr>
              ) : (
                leaderboard.map((entry, idx) => (
                  <tr key={idx}>
                    <td>{idx + 1}</td>
                    <td>{entry.name || '-'}</td>
                    <td>{entry.score || '-'}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
      <button className="btn btn-success">View Details</button>
    </div>
  );
};

export default Leaderboard;
