<template>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Codigo</th>
          <th scope="col">Nombre</th>
          <th scope="col">Cantidad</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td>{{ product.cod_product }}</td>
          <td>{{ product.name }}</td>
          <td>{{ product.cant }}</td>
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
      axios.get('http://127.0.0.1:8000/products/')
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
  