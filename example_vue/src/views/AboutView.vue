<template>
  <table class="table">
    <thead>
      <tr>
        <th scope="col">name</th>
        <th scope="col">direction</th>
        <th scope="col">clientesConsulta  </th>
        <th scope="col">prodcutosConsulta  </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="product in products" :key="product.id">
        <td>{{ product.name }}</td>
        <td>{{ product.direction }}</td>
        <td>{{ product.clientesConsulta }}</td>
        <td>{{ product.productosConsulta }}</td>
      </tr>
    </tbody>
  </table>
</template>
<script>
import axios from "axios";

export default {
  name: 'App',
  data() {
    return {
      products: []
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/allCoffeeShops/')
      .then(response => {
        console.log(response.data)
        this.products = response.data;
      })
      .catch(error => {
        console.error('Error al hacer la solicitud:', error);
      });
  }
}
</script>
