// import axios from 'axios';
import clienteAxios from "../config/axios";

export default class AdministracionApi {

    url = "http://localhost:8000";

    getProductsSmall() {
        return clienteAxios.get('assets/demo/data/products-small.json').then(res => res.data.data);
    }

    getNiveles() {
        return clienteAxios.get('/nivel/').then(res => res.data);
    }

    newNivel(nivel) {
        return clienteAxios.post('/nivel/', nivel);
    }

    updateNivel(id, nivel) {
        return clienteAxios.put(`/nivel/${id}/`, nivel);
    }

    deleteNivel(id) {
        return clienteAxios.delete(`/nivel/${id}/`);
    }

    getProductsWithOrdersSmall() {
        return clienteAxios.get('assets/demo/data/products-orders-small.json').then(res => res.data.data);
    }
}