// pages/index.js
import React from 'react';
import { useQuery } from 'react-query';
import { sendRequestToGo } from '../utils/api';

const HomePage = () => {
  const { data, error, isLoading } = useQuery('goData', sendRequestToGo);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error loading data</div>;
  }

  return (
    <div>
      <h1>Data from Go Service</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default HomePage;
