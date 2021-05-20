<template>
  <b-navbar toggleable="lg" type="light">
    <b-navbar-brand>
        <NuxtLink class="navbar-brand" to="/">
            <b-img class="navbar-brand-image" :src="require('@/assets/img/logo.png')" fluid ></b-img>
            <span class="navbar-brand-text">
                <span>
                    Monitoramento de despejos<br>
                    <small>Espírito Santo</small>
                </span>
            </span>
        </NuxtLink>
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item>
            <NuxtLink to="/" class="nav-item active">
                <span class="nav-link">Início</span>
            </NuxtLink>
        </b-nav-item>

        <b-nav-item>
            <NuxtLink to="/quem-somos/" class="nav-item">
                <span class="nav-link">Quem somos</span>
            </NuxtLink>
        </b-nav-item>

        <b-nav-item>
            <NuxtLink to="/mapeamento/" class="nav-item">
                <span class="nav-link">Mapeamento</span>
            </NuxtLink>
        </b-nav-item>

        <b-nav-item>
            <NuxtLink to="/publicacoes/" class="nav-item">
                <span class="nav-link">Publicações</span>
            </NuxtLink>
        </b-nav-item>

        <b-nav-item>
            <NuxtLink to="/denuncie/" class="nav-item">
                <span class="nav-link">Denuncie</span>
            </NuxtLink>
        </b-nav-item>

        <b-nav-item>
            <NuxtLink to="/contato/" class="nav-item">
                <span class="nav-link">Contato</span>
            </NuxtLink>
        </b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
    export default {
        
    }
</script>

<style scoped>
.navbar{
    padding-top: 0;
    padding-bottom: 0;
    background-color: rgba(211, 210, 210, 0.46);
}

.navbar-brand, .navbar-brand-image{
    padding-top: 0;
    padding-bottom: 0;
    height: 100%;
}

.navbar-brand-text {
    display: inline-block;
    text-align: center;
    vertical-align: middle;
}
</style>