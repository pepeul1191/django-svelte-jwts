<script>
  import { onMount } from 'svelte';
  import { navigate } from "svelte-routing";
  import AssetsFilters from '../../forms/AssetFilters.svelte';
  import DataTable from '../../widgets/DataTable.svelte';

  let issueDetailModalInstance;
  let issueFormInstance;
  let issueDetailModal;
  let alertMessage = {
    text: '',
    status: '',
  };
  let assetDataTable;
  let modalTitle;

  onMount(() => {
    // montar acciones de la tabla
      // ejemplos
      //assetDataTable.addButton.action = () => assetDataTable.addRow();
      //assetDataTable.addButton.action = () => assetDataTable.goToLink('/users');
      //assetDataTable.addButton.action = () => assetDataTable.goToHref(BASE_URL + 'hola');
      //assetDataTable.addButton.action = () => assetDataTable.openTab(BASE_URL + 'hola');
    
    // table action buttons
    assetDataTable.actionButtons = [
      {
        class: 'btn-secondary',
        icon: 'fa-pencil',
        label: 'Editar',
        action: editAsset
      },
      {
        class: 'btn-danger',
        icon: 'fa-trash',
        label: 'Eliminar',
        action: (record) => {
          assetDataTable.askToDeleteRow(record, 'id');
        }
      },
    ];
    assetDataTable.list();
  });

  const editAsset = (asset) => {
    alert('editAssetModal');
  }

  const handleSearchFilter = (event) => {
    const { name, description } = event.detail;
    console.log(event.detail);
    assetDataTable.queryParams = {name,description};
    assetDataTable.list();
  }
  
  const handleCleanFilter= () => {
    assetDataTable.queryParams = {};
    assetDataTable.list();
  }

  const addIssue = () => {
    alert('addAssetModal');
  }

  const handleTableAlert = (callback) => { 
    alertMessage = callback.detail;
    setTimeout(() => {
      alertMessage = {
        text: '',
        status: '',
      };
    }, 4300);
  }
</script>
<style></style>

<div class="container my-2">
  <div class="row">
    <h1 class="mb-2 subtitle">Gestión de Activos</h1>
  </div>
  <hr>
  {#if alertMessage.text != ''}
    <div class="alert alert-{alertMessage.status}" role="alert">
      {alertMessage.text}
    </div>
  {/if}
  <div class="container">
    <AssetsFilters 
      on:search={handleSearchFilter} 
      on:clean={handleCleanFilter} />
  </div>
  <div class="row subtitle-row">
    <h4 class="subtitle">Listado de Activos</h4>
  </div>
  <div class="container">
    <DataTable 
      bind:this={assetDataTable}
      fetchURL={URLS.TICKETS_SERVICE + 'api/v1/assets'}
      tokenStorageId={'jwtTicketsToken'}
      columnKeys={['_id', 'name', 'description']}
      columnTypes={['id', 'td', 'td']}
      columnNames={['ID', 'Nombre', 'Descripción', 'Acciones']}
      columnStyles={['max-width: 50px;', 'max-width: 250px;', 'max-width: 150px;']}
      columnClasses={['d-none', '', '', 'text-end']}
      tdStyles={['max-width: 50px;', 'max-width: 250px;', 'max-width: 150px;']}
      messages = {{
        success: 'Datos actualizados', 
        errorNetwork: 'No se pudo listar los sistemas. No hay conexión con el servidor.',
        notFound: 'No se pudo listar los sistemas. Recurso no encontrado.', 
        serverError:'No se pudo listar los sistemas. Error interno del servidor',
        requestError: 'No se pudo listar los sistemas. No se recibió respuesta del servidor',
        otherError: 'No se pudo listar los sistemas. Ocurrió un error no esperado al traer los datos del servidor',
      }}
      addButton={{
        display: true,
        disabled: false,
        action: addIssue
      }}
      pagination = {{
        display: true,
        step: 10,
        totalPages: 0,
        actualPage: 1
      }}
      actionButtons={[]} 
      on:alert={handleTableAlert}
    />
  </div>
</div>