<script>
  import { Router, Route, navigate } from 'svelte-routing';
  import Home from '../pages/app/Home.svelte';
  import Asste from '../pages/app/Asset.svelte';
  import Issue from '../pages/app/Issue.svelte';
  import IssueDetail from '../pages/app/IssueDetail.svelte';
  import Employee from '../pages/app/Employee.svelte';
	import Asset from '../pages/app/Asset.svelte';
  export let basepath = '/';

  const signOut = (e) => {
    e.preventDefault();
    // Borrar los tokens del localStorage
    localStorage.removeItem('jwtAccessToken');
    localStorage.removeItem('jwtFilesToken');
    // Redirigir a /sign-out
    window.location.href = '/sign-out';
  };
</script>
  
<style></style>

<!-- Barra de Navegación -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="/" on:click|preventDefault={() => {navigate('/')}}>Tickets  </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <a class="nav-link" href="/employees" on:click|preventDefault={() => {navigate('/employees')}}>Colaboradores</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/assets" on:click|preventDefault={() => {navigate('/assets')}}>Activos</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/issues" on:click|preventDefault={() => {navigate('/issues')}}>Incidencias</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/sign-out" on:click={signOut}>Salir</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<Router basepath="{basepath}">
  <Route path="/" component={Home} />
  <Route path="/assets" component={Asset} />
  <Route path="/issues" component={Issue} />
  <Route path="/employees" component={Employee} />
  <Route path="/issues/new" component={IssueDetail} />
  <Route path="/issues/edit/:_id" let:params><IssueDetail _id={params._id}/></Route>
</Router>

<!-- Pie de Página -->
<footer class="bg-dark text-white text-center py-3">
  <p>&copy; 2024 Mi Sitio. Todos los derechos reservados.</p>
</footer>