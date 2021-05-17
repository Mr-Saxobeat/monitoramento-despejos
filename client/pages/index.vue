<template>
  <div class="container-fluid">
    <div class="hero-image">
      <div class="hero-text row">
        <NuxtLink to="/denuncie/" class="nav-item col-sm">
            <span class="nav-link"><div class="" style="color: #D1520F; font-size: 35px"><strong>DENUNCIE</strong></div></span>
        </NuxtLink>

        <NuxtLink to="/mapeamento/" class="col-sm">
          <div  style="color: #111111; font-size: 25px">Mapeamento de despejos<br>no Espírito Santo</div>
        </NuxtLink>

        <NuxtLink to="/publicacoes/" class="col-sm">
          <div  style="color: #000000; font-size: 25px">Conheça seus direitos</div>
        </NuxtLink>
      </div>  
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.hero-image {
  height: 100%;
  width: 100%;
  background-image: url('~assets/img/foto-crianca.jpg');
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}

.hero-text {
  height: 110px;
  width: 100%;
  margin: 0;
  padding: 0;
  text-align: center;
  position: absolute;
  color: white;
  bottom: 0;
  background-color: rgba(211, 210, 210, 0.6);
}

.hero-text .col-sm {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>