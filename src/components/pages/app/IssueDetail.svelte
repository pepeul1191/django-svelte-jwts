<script>
  import { onMount } from 'svelte';
	import IssueHeaderTab from '../../forms/IssueHeaderTab.svelte';

  export let title = 'Nueva Incidencia';
  let issueDetailModalInstance;
  let issueFormInstance;
  let issueDetailModal;
  let alertMessage = {
    text: '',
    status: '',
  };
  
  let modalTitle;

  onMount(() => {
    // montar acciones de la tabla
      // ejemplos
      //issueDataTable.addButton.action = () => issueDataTable.addRow();
      //issueDataTable.addButton.action = () => issueDataTable.goToLink('/users');
      //issueDataTable.addButton.action = () => issueDataTable.goToHref(BASE_URL + 'hola');
      //issueDataTable.addButton.action = () => issueDataTable.openTab(BASE_URL + 'hola');    
  });

</script>
<style></style>

<div class="container my-2">
  <div class="row">
    <h1 class="mb-2 subtitle">{title}</h1>
  </div>
  <hr>
  {#if alertMessage.text != ''}
    <div class="alert alert-{alertMessage.status}" role="alert">
      {alertMessage.text}
    </div>
  {/if}
  <ul class="nav nav-tabs mb-3" id="myTabs" role="tablist">
    <li class="nav-item" role="presentation">
      <button class="nav-link active" id="generales-tab" data-bs-toggle="tab" data-bs-target="#header" type="button" role="tab">
        Datos Generales
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="etiquetas-tab" data-bs-toggle="tab" data-bs-target="#assets" type="button" role="tab">
        Activos Asociados
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="documentos-tab" data-bs-toggle="tab" data-bs-target="#users" type="button" role="tab">
        Acceso a Usuarios
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="documentos-tab" data-bs-toggle="tab" data-bs-target="#histories" type="button" role="tab">
        Seguimiento e Historial
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="documentos-tab" data-bs-toggle="tab" data-bs-target="#logs" type="button" role="tab">
        Actividad de Usuarios
      </button>
    </li>
  </ul>
  <div class="tab-content">
    <div class="tab-pane fade show active" id="header" role="tabpanel">
      <IssueHeaderTab />
    </div>
    <div class="tab-pane fade" id="assets" role="tabpanel">
      <div class="row subtitle-row mt-3">
        <h4 class="subtitle">Documentos</h4>
      </div>
    </div>
    <div class="tab-pane fade" id="users" role="tabpanel">
      <div class="row subtitle-row mt-3">
        <h4 class="subtitle">Usuarios</h4>
      </div>
    </div>
    <div class="tab-pane fade" id="histories" role="tabpanel">
      <div class="row subtitle-row mt-3">
        <h4 class="subtitle">Historias</h4>
      </div>
    </div>
    <div class="tab-pane fade" id="logs" role="tabpanel">
      <div class="row subtitle-row mt-3">
        <h4 class="subtitle">Actividad de Usuarios</h4>
      </div>
    </div>
  </div>
</div>