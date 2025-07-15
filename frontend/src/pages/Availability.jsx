import React from 'react';
import { useAvailability } from '../hooks/useAvailability';

export default function Availability() {
  const { data, isLoading, isError } = useAvailability();

  if (isLoading) return <p>Loading availability…</p>;
  if (isError) return <p className="text-red-600">Error loading data.</p>;

  return (
    <div>
      <h2 className="text-2xl font-semibold mb-4">Parking Availability</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {data.map(slot => (
          <div
            key={slot.id}
            className={`p-4 rounded shadow ${
              slot.available ? 'bg-green-100' : 'bg-red-100'
            }`}
          >
            <h3 className="font-bold">Slot {slot.id}</h3>
            <p>Status: {slot.available ? 'Available' : 'Occupied'}</p>
            {slot.available && (
              <button className="mt-2 px-3 py-1 bg-blue-600 text-white rounded">
                Reserve
              </button>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

