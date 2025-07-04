<script>
  import { onMount } from 'svelte';
  import { navigate } from "svelte-routing";
  import IssueFilters from '../../forms/IssueFilters.svelte';
  import DataTable from '../../widgets/DataTable.svelte';

  let issueDetailModalInstance;
  let issueFormInstance;
  let issueDetailModal;
  let alertMessage = {
    text: '',
    status: '',
  };
  let issueDataTable;
  let modalTitle;

  onMount(() => {
    // montar acciones de la tabla
      // ejemplos
      //issueDataTable.addButton.action = () => issueDataTable.addRow();
      //issueDataTable.addButton.action = () => issueDataTable.goToLink('/users');
      //issueDataTable.addButton.action = () => issueDataTable.goToHref(BASE_URL + 'hola');
      //issueDataTable.addButton.action = () => issueDataTable.openTab(BASE_URL + 'hola');
    
    // table action buttons
    issueDataTable.actionButtons = [
      {
        class: 'btn-secondary',
        icon: 'fa-pencil',
        label: 'Editar',
        action: editIssue
      },
      {
        class: 'btn-danger',
        icon: 'fa-trash',
        label: 'Eliminar',
        action: (record) => {
          issueDataTable.askToDeleteRow(record, 'id');
        }
      },
    ];
    issueDataTable.list();
  });

  const editIssue = (issue) => {
    navigate(`/issues/edit/${issue._id}`);
  }

  const handleSearchFilter = (event) => {
    //const { name, description } = event.detail;
    console.log(event.detail);
    //systemDataTable.queryParams = {name,description};
    //systemDataTable.list();
  }
  
  const handleCleanFilter= () => {
    systemDataTable.queryParams = {};
    systemDataTable.list();
  }

  const addIssue = () => {
    navigate(`/issues/new`);
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
    <h1 class="mb-2 subtitle">Gestión de Incidencias</h1>
  </div>
  <hr>
  {#if alertMessage.text != ''}
    <div class="alert alert-{alertMessage.status}" role="alert">
      {alertMessage.text}
    </div>
  {/if}
  <div class="container">
    <IssueFilters 
      on:search={handleSearchFilter} 
      on:clean={handleCleanFilter} />
  </div>
  <div class="row subtitle-row">
    <h4 class="subtitle">Listado de Sistemas</h4>
  </div>
  <div class="container">
    <DataTable 
      bind:this={issueDataTable}
      fetchURL={URLS.TICKETS_SERVICE + 'api/v1/issues/summary'}
      tokenStorageId={'jwtTicketsToken'}
      columnKeys={['_id', 'resume', 'reporter.name', 'reportered', 'priority.name', 'issue_state.name']}
      columnTypes={['id', 'td', 'td']}
      columnNames={['ID', 'Resumen', 'Reportado por', 'Fecha', 'Prioridad', 'Estado', 'Acciones']}
      columnStyles={['max-width: 50px;', 'max-width: 250px;', 'max-width: 400px;', 'max-width: 150px;']}
      columnClasses={['d-none', '', '', '','','','text-end']}
      tdStyles={['max-width: 50px;', 'max-width: 250px;', 'max-width: 400px;', 'max-width: 150px;']}
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
        display: false,
        step: 10,
        totalPages: 0,
        actualPage: 1
      }}
      actionButtons={[]} 
      on:alert={handleTableAlert}
    />
  </div>
</div>