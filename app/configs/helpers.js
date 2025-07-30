// app/config/helpers.js

import axios from 'axios';

// Función para hacer login y obtener los tokens desde los servicios externos
export const login = async (username, password) => {
  const answer = { body: {}, status: 200 };

  try {
    // Petición a la API de acceso
    const accessResponse = await axios.post(
      `${process.env.URL_ACCESS_SERVICE}api/v1/auth/by-username`,
      {
        username,
        password,
        system_id: 1
      },
      {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'X-Auth-Trigger': process.env.X_AUTH_ACCESS_SERVICE
        }
      }
    );

    if (accessResponse.status === 200) {
      const tmp = accessResponse.data;
      console.log(tmp)
      answer.body.id = tmp.id;
      answer.body.username = tmp.username;
      answer.body.email = tmp.email;
      answer.body.tokens = {};
      answer.body.tokens.access = tmp.token;
      answer.body.email = tmp.email;

      // Petición a la API de archivos
      const filesResponse = await axios.post(
        `${process.env.URL_FILES_SERVICE}api/v1/auth/generate-token`,
        {
          user: {
            id: answer.body.id,
            username: answer.body.username,
            email: answer.body.email
          }
        },
        {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Auth-Trigger': process.env.X_AUTH_FILES_SERVICE
          }
        }
      );

      // Petición a la API de tickets
      const ticketsResponse = await axios.post(
        `${process.env.URL_TICKETS_SERVICE}api/v1/auth/generate-token`,
        {
          user: {
            id: answer.body.id,
            username: answer.body.username,
            email: answer.body.email
          }
        },
        {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Auth-Trigger': process.env.X_AUTH_TICKETS_SERVICE
          }
        }
      );

      // Combinar respuestas de servicios externos
      if (filesResponse.status === 200 && ticketsResponse.status === 200) {
        answer.body.tokens.files = filesResponse.data.token;
        answer.body.tokens.tickets = ticketsResponse.data.token;
      } else {
        const tmpMessage = `${filesResponse.data.message}, ${ticketsResponse.data.message}`;
        answer.body.error = tmpMessage;
        answer.body.message = 'Error al autenticarse con los servicios';
        answer.status = 400;
      }
    } else {
      answer.body.error = accessResponse.data.message;
      answer.body.message = accessResponse.data.error;
      answer.status = accessResponse.status;
    }
  } catch (error) {
    if (error.response) {
      // Si el error es de una solicitud externa
      answer.body.error = error.response.data.message || error.message;
      answer.body.message = 'Error al contactar con la API externa';
      answer.status = error.response.status;
    } else {
      // Errores generales
      answer.body.error = 'Ocurrió un error al generar los JWTs';
      answer.body.message = error.message;
      answer.status = 500;
    }
  }

  return answer;
}
