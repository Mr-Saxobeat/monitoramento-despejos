<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light justify-content-center">
            <ul class="navbar-nav">
                <NuxtLink class="navbar-brand" to="/">
                    <b-img :src="require('@/assets/img/logo.png')" fluid class="logo"></b-img>
                    Monitoramento de despejos
                </NuxtLink>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarNav">
                    <NuxtLink to="/" class="nav-item active">
                        <span class="nav-link">Início</span>
                    </NuxtLink>
                    <NuxtLink to="quem-somos/" class="nav-item">
                        <span class="nav-link">Quem somos</span>
                    </NuxtLink>
                    <NuxtLink to="mapeamento/" class="nav-item">
                        <span class="nav-link">Mapeamento</span>
                    </NuxtLink>
                    <NuxtLink to="publicacoes/" class="nav-item">
                        <span class="nav-link">Publicações</span>
                    </NuxtLink>
                    <NuxtLink to="denuncie/" class="nav-item">
                        <span class="nav-link">Denuncie</span>
                    </NuxtLink>
                    <NuxtLink to="contato/" class="nav-item">
                        <span class="nav-link">Contato</span>
                    </NuxtLink>
                </div>
            </ul>
    </nav>
</template>

<script>
    export default {
        
    }
</script>

<style scoped>
nav {
    padding: 0;
    margin: auto;
    background-color: rgba(211, 210, 210, 0.46);
}
.logo {
    width: 100px;
    height: 100px;
}
</style>