import axios from 'axios';

export const create = (baseURL, tokenKey, data) => {
  return new Promise((resolve, reject) => {
    const token = localStorage.getItem(tokenKey);
    axios.post(baseURL + 'api/v1/issues', data, {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      }
    })
    .then(function (response) {
      resolve(response);
    })
    .catch(function (error) {
      if (error.response?.status === 404) {
        console.error('Miembro no encontrado');
      } else {
        console.error(error.response?.data || error.message);
      }
      reject(error.response);
    });
  });
}
