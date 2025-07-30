<script>
  import { navigate } from 'svelte-routing';

  export let userType;
  export let activeLink;
</script>

<div class="sidebar d-none d-md-block">
  <div class="sidebar-header">
    <a class="navbar-brand text-dark" href="/" on:click|preventDefault={() => {navigate('/')}}>Gestión de Tickets</a>
  </div>
  <ul class="nav flex-column mt-3">
    <li class="nav-item">
      <a class="nav-link" class:active={activeLink === '/'} href="/" on:click|preventDefault={() => {navigate('/')}}>
        <i class="fa fa-tachometer-alt me-2"></i> Dashboard
      </a>
    </li>

    <li class="nav-item">
      <a class="nav-link" class:active={activeLink === '/assets'} href="/assets" on:click|preventDefault={() => {navigate('/assets')}}>
        <i class="fa fa-cogs me-2"></i> Activos
      </a>
    </li>

    <li class="nav-item">
      <a class="nav-link" class:active={activeLink === '/issues'} href="/issues" on:click|preventDefault={() => {navigate('/issues')}}>
        <i class="fa fa-bug me-2"></i> Incidencias
      </a>
    </li>

    <li class="nav-item">
      <a class="nav-link" class:active={activeLink === '/tags'} href="/tags" on:click|preventDefault={() => {navigate('/tags')}}>
        <i class="fa fa-tags me-2"></i> Etiquetas
      </a>
    </li>

    <li class="nav-item">
      <a class="nav-link" class:active={activeLink === '/employees'} href="/employees" on:click|preventDefault={() => {navigate('/employees')}}>
        <i class="fa fa-users me-2"></i> Colaboradores
      </a>
    </li>

    <!-- Rutas específicas para Admin -->
    {#if userType === 'admin'}
      <li class="nav-item">
        <a class="nav-link" href="#">
          <i class="fa fa-user-shield me-2"></i> Usuarios
        </a>
      </li>
    {/if}

    <!-- Rutas para Nueva Incidencia -->
    <li class="nav-item">
      <a class="nav-link" href="/issues/new" on:click|preventDefault={() => {navigate('/issues/new')}}>
        <i class="fa fa-plus-circle me-2"></i> Nueva Incidencia
      </a>
    </li>
  </ul>
</div>
