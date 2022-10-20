// export default class ProductService {

//     getProductsSmall() {
// 		return fetch('data/products-small.json').then(res => res.json()).then(d => d.data);
// 	}

// 	getProducts() {
// 		return fetch('data/products.json').then(res => res.json()).then(d => d.data);
//     }

//     getProductsWithOrdersSmall() {
// 		return fetch('data/products-orders-small.json').then(res => res.json()).then(d => d.data);
// 	}
	
// }

import axios from 'axios';

export default class ProductService {

    getProductsSmall() {
        return axios.get('assets/demo/data/products-small.json').then(res => res.data.data);
    }

    getProducts() {
        return axios.get('http://localhost:8000/alumno/').then(res => res.data);
    }

    getProductsWithOrdersSmall() {
        return axios.get('assets/demo/data/products-orders-small.json').then(res => res.data.data);
    }
}