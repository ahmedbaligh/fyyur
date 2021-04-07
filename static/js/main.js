// Delete Venue
const deleteVenue = async () => {
  const deleteButton = document.getElementById('delete-venue');

  const { id } = deleteButton.dataset;

  const result = await fetch(`/venues/${id}`, {
    method: 'DELETE'
  });

  if (result.status === 200) window.location.replace('/');
};
