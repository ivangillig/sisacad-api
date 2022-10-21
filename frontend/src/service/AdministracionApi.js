import axios from 'axios';

export default class AdministracionApi {

    getProductsSmall() {
        return axios.get('assets/demo/data/products-small.json').then(res => res.data.data);
    }

    getNiveles() {
        return axios.get('http://localhost:8000/api/nivel/').then(res => res.data);
    }

    newNivel(nivel) {
        return axios.post('http://localhost:8000/api/nivel/', nivel).then(res => res.data);
    }

    getProductsWithOrdersSmall() {
        return axios.get('assets/demo/data/products-orders-small.json').then(res => res.data.data);
    }
}