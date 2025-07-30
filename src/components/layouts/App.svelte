<script>
  import { Router, Route, navigate } from 'svelte-routing';
  import { onMount } from 'svelte';
  import Home from '../pages/app/Home.svelte';
  import Asste from '../pages/app/Asset.svelte';
  import Issue from '../pages/app/Issue.svelte';
  import IssueDetail from '../pages/app/IssueDetail.svelte';
  import Employee from '../pages/app/Employee.svelte';
  import Tag from '../pages/app/Tag.svelte';
	import Asset from '../pages/app/Asset.svelte';
  export let basepath = '/';

  const fetchTokensIfMissing = () => {
    // Verificar si los tokens ya existen
    var jwtToken = localStorage.getItem('jwtToken');

    // Si ambos tokens ya están guardados, no hacer nada
    if (jwtToken) {
      console.log('Token ya existen en localStorage.');
      return Promise.resolve(); // Salir sin hacer la petición
    }

    // Si alguno falta, hacer el GET a /tokens
    return new Promise(function(resolve, reject) {
      var xhr = new XMLHttpRequest();
      xhr.open('GET', '/session', true);
      xhr.setRequestHeader('Content-Type', 'application/json');
      
      xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
          var response = JSON.parse(xhr.responseText);
          var tokens = response.tokens;
          console.log(tokens)

          // Guardar ambos tokens en localStorage
          if (tokens) {
            localStorage.setItem('jwtTicketsToken', tokens.tickets);
            localStorage.setItem('jwtFilesToken', tokens.files);
            localStorage.setItem('jwtAccessToken', tokens.access);
          }

          console.log('Token guardado en localStorage.');
          resolve();
        } else {
          reject(new Error('Error HTTP: ' + xhr.status));
        }
      };

      xhr.onerror = function() {
        reject(new Error('Error de red'));
      };

      xhr.send();
    })
    .catch(function(error) {
      console.error('Error al obtener tokens:', error);
      return Promise.reject(error);
    });
  }

  onMount(() => {
    fetchTokensIfMissing()
      .then(function() {
        console.log('Tokens listos para usar.');
      })
      .catch(function(err) {
        console.error('No se pudieron obtener los tokens:', err);
      });
  });
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
          <a class="nav-link" href="/tags" on:click|preventDefault={() => {navigate('/tags')}}>Etiquetas</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/issues" on:click|preventDefault={() => {navigate('/issues')}}>Incidencias</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/sign-out">Salir</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<Router basepath="{basepath}">
  <Route path="/" component={Home} />
  <Route path="/assets" component={Asset} />
  <Route path="/issues" component={Issue} />
  <Route path="/tags" component={Tag} />
  <Route path="/employees" component={Employee} />
  <Route path="/issues/new" component={IssueDetail} />
  <Route path="/issues/edit/:_id" let:params><IssueDetail _id={params._id}/></Route>
</Router>

<!-- Pie de Página -->
<footer class="bg-dark text-white text-center py-3">
  <p>&copy; 2024 Mi Sitio. Todos los derechos reservados.</p>
</footer>