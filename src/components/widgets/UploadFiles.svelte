<svelte:options accessors={true} />
<script>
  import { onMount } from 'svelte';
  //import { deleteOne } from '../../../services/app/files_service'; // Asegúrate de importar tu servicio

  let files = [];
  let textInput = '';
  let fileInput = null;
  let responseMessage = '';
  let isLoading = false;

  export let postURL = '';
  export let tokenStorageId = '';
  export let extraData = {};

  const fileChange = (event) => {
    const { name, value } = event.target;

    if (name === 'file') {
      fileInput = event.target.files[0]; // Guardamos el archivo seleccionado
    } else {
      textInput = value; // Guardamos el texto del input
    }
  };

  export const setExtraData = (data) => {
    extraData = data;
  };

  const uploadFile = async () => {
    if (!fileInput) {
      alert('Por favor, selecciona un archivo');
      return;
    }

    isLoading = true;
    responseMessage = '';

    const formData = new FormData();
    formData.append('file', fileInput);
    formData.append('name', textInput);

    // Agregar datos adicionales dinámicamente
    console.log(extraData)
    for (const [key, value] of Object.entries(extraData || {})) {
      formData.append(key, value);
    }

    const token = localStorage.getItem(tokenStorageId); // Obtén el JWT

    try {
      console.log(postURL)
      const res = await fetch(postURL, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${token}`
          // No establezcas Content-Type con FormData
        },
        body: formData,
        credentials: 'include'
      });

      if (!res.ok) throw new Error(`Error del servidor: ${res.status}`);
      const data = await res.json();

      // Actualizamos la lista de archivos si recibimos uno nuevo
      if (data.file) {
        files = [...files, data.file];
      }

      responseMessage = `✅ Éxito: ${JSON.stringify(data)}`;
    } catch (err) {
      responseMessage = `❌ Error: ${err.message}`;
    } finally {
      isLoading = false;
    }
  };

  const deleteFile = (_id) => {
    return async () => {
      try {
        /*
        await deleteOne(_id);
        files = files.filter(item => item._id !== _id);
        messageImageAlert.show = true;
        messageImageAlert.message = `Se eliminó la imagen del artículo`;
        messageImageAlert.class = 'success';
        */
        setTimeout(() => {
          messageImageAlert.show = false;
        }, 5000);
      } catch (error) {
        console.error('Error al eliminar:', error);
        messageImageAlert.show = true;
        messageImageAlert.message = `Error al eliminar: ${error.message}`;
        messageImageAlert.class = 'danger';
      }
    };
  };

  let messageImageAlert = {
    show: false,
    message: '',
    class: ''
  };
</script>

<style>
  .file {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
</style>

<div class="container">
  <div class="mb-12">
    <div class="row">
      <div class="col-md-5">
        <input type="file" class="form-control" id="formFile" name="file" on:change={fileChange} />
      </div>
      <div class="col-md-5">
        <input
          type="text"
          class="form-control ms-2"
          placeholder="Nombre del archivo"
          id="fileName"
          name="name"
          bind:value={textInput}
          on:input={fileChange}
        />
      </div>
      <div class="col-md-2 d-flex justify-content-end align-items-end">
        <button type="button" class="btn btn-primary ms-3" on:click={uploadFile} disabled={isLoading}>
          <span><i class="fa fa-upload"></i> Subir Archivo</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Mensaje de respuesta -->
  {#if responseMessage}
    <div class="alert alert-info">{responseMessage}</div>
  {/if}

  <div class="mb-12">
    {#each files as file (file._id)}
      <div class="alert alert-secondary file" role="alert">
        <div class="row align-items-center">
          <div class="col-auto">
            <a href="/{file.url}" target="_blank" rel="noopener noreferrer">
              <img src="/{file.url}" alt="{file.name}" height="50" width="50" />
            </a>
          </div>
          <div class="col">
            {file.name}<br>
            <small><b>{new Date(file.created).toLocaleString()}</b></small>
          </div>
          <div class="col-auto">
            <button class="btn btn-danger" on:click={deleteFile(file._id)}>
              <i class="fa fa-times"></i>
            </button>
          </div>
        </div>
      </div>
    {/each}
  </div>
</div>