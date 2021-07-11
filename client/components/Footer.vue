<template>
  <div class="footer">
      <ul>
            <li> 
                <NuxtLink to="/contato/" class="nav-item">
                    <span class="nav-link">Contato</span>
                </NuxtLink>
            </li>

            <li>
                <NuxtLink to="/quem-somos/" class="nav-item">
                    <span class="nav-link">Quem somos</span>
                </NuxtLink>
            </li>

            <li>
                <NuxtLink to="/quem-somos/" class="nav-item">
                    <span class="nav-link">Instagram EMAU</span>
                </NuxtLink>
            </li>

            <li>
                <NuxtLink to="/quem-somos/" class="nav-item">
                    <span class="nav-link">Instagram Despejo Zero</span>
                </NuxtLink>
            </li>
      </ul>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.footer{
    margin: 0;
    background-color: #100F0E;
    text-align: center;
}

ul {
    list-style: none;
    color: #FFFFFF;
}

ul li {
    padding-bottom: 0px;
}

a, a:hover {
    color: #FFFFFF;
    text-decoration: none;
    padding: 0;
}

.nav-link  {
    padding: 0;
}
</style>