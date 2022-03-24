export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  image: string;
  link: string;
  gallery: string[];
  rating: number;
  category: string;
  NumberLikes: number;
}

export const categories = ["iPhone", "Samsung", "Google Pixel", "Tracfone", "Old phone"];

export const products = [
  {
    id: 0,
    name: 'iPhone 12 Pro',
    price: 799,
    description: 'A large phone with one of the best screens',
    image: 'https://m.media-amazon.com/images/I/712yl2wTDbL._AC_SX679_.jpg',
    link: 'https://www.amazon.com/Apple-iPhone-12-Pro-Pacific/dp/B09JFN8K6T/ref=sr_1_1?crid=O3K1RV3ZZJ1K&keywords=iphone+12&qid=1647967576&sprefix=iphone+1%2Caps%2C264&sr=8-1',
    gallery: ['https://avatars.mds.yandex.net/i?id=2a00000179fa1fa57f4b9078c4c1c4d9f2c3-4378134-images-thumbs&n=13',
              'https://avatars.mds.yandex.net/i?id=165ff7cbf97cc105838f2fa113871e48-5883346-images-thumbs&n=13',
              'https://avatars.mds.yandex.net/i?id=8123c8cb5e39f26cd74cf70bf474e0ca-5483025-images-thumbs&n=13'
              ],
    rating: 4.5,
    category: 'iPhone',
    NumberLikes: 0
  },
  {
    id: 1,
    name: 'Google Pixel 6',
    price: 699,
    description: 'A great phone with one of the best cameras',
    image: 'https://m.media-amazon.com/images/I/61oQtjPpM-L._AC_SX466_.jpg',
    link: 'https://www.amazon.com/Google-Pixel-Unlocked-Smartphone-Ultrawide/dp/B09HJZPFDD/ref=sr_1_1?crid=1I9K6GX6ERV4J&keywords=google+pixel+6&qid=1647967603&sprefix=google+pixel+%2Caps%2C234&sr=8-1',
    gallery: ['https://m.media-amazon.com/images/I/61oQtjPpM-L._AC_SX466_.jpg'],
    rating: 4.0,
    category: 'Google Pixel',
    NumberLikes: 0
  },
  {
    id: 2,
    name: 'Samsung Galaxy S22',
    price: 299,
    description: 'A cool phone with beatiful design',
    image: 'https://m.media-amazon.com/images/I/61U6oC65TTL._AC_SX466_.jpg',
    link: 'https://www.amazon.com/Samsung-Smartphone-Unlocked-Brightest-Processor/dp/B09MVZSW5V/ref=sr_1_2?crid=TR37DK0OUHOD&keywords=samsung+galaxy+s22+ultra&qid=1647965303&sprefix=Samsung%2Caps%2C233&sr=8-2',
    gallery: ['https://m.media-amazon.com/images/I/61U6oC65TTL._AC_SX466_.jpg'],
    rating: 3.0,
    category: 'Samsung',
    NumberLikes: 0
  },
  {
    id: 3,
    name: 'TracFone Blu',
    price: 499,
    description: 'This phone is locked to Tracfone, which means this device can only be used on the Tracfone wireless network.',
    image: 'https://m.media-amazon.com/images/I/7150tUunFnL._AC_SX679_.jpg',
    link: 'https://www.amazon.com/Samsung-Smartphone-Unlocked-Brightest-Processor/dp/B09MVZSW5V/ref=sr_1_2?crid=TR37DK0OUHOD&keywords=samsung+galaxy+s22+ultra&qid=1647965303&sprefix=Samsung%2Caps%2C233&sr=8-2',
    gallery: ['https://m.media-amazon.com/images/I/7150tUunFnL._AC_SX679_.jpg'],
    rating: 3.0,
    category: 'Tracfone',
    NumberLikes: 0
  },
  {
    id: 4,
    name: 'AT&T BL102-3 DECT 6.0',
    price: 199,
    description: 'A cool phone with beatiful design',
    image: 'https://m.media-amazon.com/images/I/81xDumBYGBL._AC_SX466_.jpg',
    link: 'https://www.amazon.com/AT-BL102-3-3-Handset-Answering-Unsurpassed/dp/B086QCGQ8C/ref=sr_1_8?crid=2BF0J9N361HVQ&keywords=phone&qid=1647966949&sprefix=ph%2Caps%2C346&sr=8-8',
    gallery: ['https://m.media-amazon.com/images/I/81xDumBYGBL._AC_SX466_.jpg'],
    rating: 1.5,
    category: 'Old phone',
    NumberLikes: 0
  },
  {
    id: 5,
    name: 'Tracfone Samsung Galaxy A12',
    price: 299,
    description: 'A cool phone with beatiful design',
    image: 'https://m.media-amazon.com/images/I/81pl3Tc9kTL._AC_SX679_.jpg',
    link: 'https://www.amazon.com/Samsung-Smartphone-Unlocked-Brightest-Processor/dp/B09MVZSW5V/ref=sr_1_2?crid=TR37DK0OUHOD&keywords=samsung+galaxy+s22+ultra&qid=1647965303&sprefix=Samsung%2Caps%2C233&sr=8-2',
    gallery: ['https://m.media-amazon.com/images/I/81pl3Tc9kTL._AC_SX679_.jpg'],
    rating: 3.3,
    category: 'Tracfone',
    NumberLikes: 0
  },
  {
    id: 6,
    name: 'Future Call FC-0613',
    price: 299,
    description: 'A cool phone with beatiful design',
    image: 'https://m.media-amazon.com/images/I/81ge4foQYdL._AC_SX466_.jpg',
    link: 'https://www.amazon.com/Future-Call-FC-0613-Picture-Protection/dp/B0797JGC34/ref=sr_1_15_sspa?crid=2BF0J9N361HVQ&keywords=phone&qid=1647966949&sprefix=ph%2Caps%2C346&sr=8-15-spons&psc=1&smid=AWMCFB3232K8Z&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOVdWTzRYQTRCUU04JmVuY3J5cHRlZElkPUEwMDEzMzYyMUc4UVhXN1ZUSzgyQyZlbmNyeXB0ZWRBZElkPUEwOTMwMDU0M0wxRUZBMzBINVA1WiZ3aWRnZXROYW1lPXNwX210ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=',
    gallery: ['https://m.media-amazon.com/images/I/81ge4foQYdL._AC_SX466_.jpg'],
    rating: 1.0,
    category: 'Old phone',
    NumberLikes: 0
  },
  {
    id: 7,
    name: 'Corded Phone',
    price: 299,
    description: ' UNLIKE OTHER LAND LINE TELEPHONES for home that DON’T PICK UP VOICES well and make it HARDER – NOT EASIER – TO HEAR the person on the other end of the line',
    image: 'https://m.media-amazon.com/images/I/61gQlZn8REL._AC_SX466_.jpg',
    link: 'https://www.amazon.com/Trimline-Corded-Phone-impaired-Telephone/dp/B00CTC9QGG/ref=sr_1_20_sspa?crid=2BF0J9N361HVQ&keywords=phone&qid=1647966949&sprefix=ph%2Caps%2C346&sr=8-20-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOVdWTzRYQTRCUU04JmVuY3J5cHRlZElkPUEwMDEzMzYyMUc4UVhXN1ZUSzgyQyZlbmNyeXB0ZWRBZElkPUEwNzYyODg0M0FMSjUwOVI5U0dRSyZ3aWRnZXROYW1lPXNwX2J0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1',
    gallery: ['https://m.media-amazon.com/images/I/61gQlZn8REL._AC_SX466_.jpg'],
    rating: 5.0,
    category: 'Old phone',
    NumberLikes: 0
  },
  {
    id: 8,
    name: 'AT&T DL72219',
    price: 299,
    description: 'Long Range - Experience the best in long-range coverage and clarity, provided by a unique antenna design and advances in noise-filtering technology.',
    image: 'https://m.media-amazon.com/images/I/81zKUmUOwwL._AC_SX466_.jpg',
    link: 'https://www.amazon.com/Samsung-Smartphone-Unlocked-Brightest-Processor/dp/B09MVZSW5V/ref=sr_1_2?crid=TR37DK0OUHOD&keywords=samsung+galaxy+s22+ultra&qid=1647965303&sprefix=Samsung%2Caps%2C233&sr=8-2',
    gallery: ['https://m.media-amazon.com/images/I/81zKUmUOwwL._AC_SX466_.jpg'],
    rating: 3.5,
    category: 'Old phone',
    NumberLikes: 0
  },
  {
    id: 9,
    name: 'AT&T 210 Basic Trimline Corded Phone',
    price: 299,
    description: 'Products with electrical plugs are designed for use in the US. Outlets and voltage differ internationally and this product may require an adapter or converter for use in your destination. Please check compatibility before purchasing.',
    image: 'https://m.media-amazon.com/images/I/51KynNOuTeL._AC_SX466_.jpg',
    link: 'https://www.amazon.com/Samsung-Smartphone-Unlocked-Brightest-Processor/dp/B09MVZSW5V/ref=sr_1_2?crid=TR37DK0OUHOD&keywords=samsung+galaxy+s22+ultra&qid=1647965303&sprefix=Samsung%2Caps%2C233&sr=8-2',
    gallery: ['https://m.media-amazon.com/images/I/51KynNOuTeL._AC_SX466_.jpg'],
    rating: 3.0,
    category: 'Old phone',
    NumberLikes: 0
  },
  {
    id: 10,
    name: 'iPhone 11 Pro',
    price: 699,
    description: 'A like-new experience. Backed by a one-year satisfaction guarantee.',
    image: 'https://m.media-amazon.com/images/I/81AaNJqE+wS._AC_SY741_.jpg',
    link: 'https://www.amazon.com/Apple-iPhone-256GB-Midnight-Green/dp/B08BHXC5ZS/ref=sr_1_2?crid=2E6IHFARNG7V2&keywords=iphone+13&qid=1648052512&sprefix=iphone+1%2Caps%2C273&sr=8-2',
    gallery: ['https://m.media-amazon.com/images/I/81AaNJqE+wS._AC_SY741_.jpg'],
    rating: 4.7,
    category: 'iPhone',
    NumberLikes: 0
  },
  {
    id: 11,
    name: 'Google Pixel 5',
    price: 650,
    description: 'The high quality display with Dynamic AMOLED 2X delivers vibrant color and brightness, even in bright sunlight',
    image: 'https://m.media-amazon.com/images/I/81-fNmQqlLL._AC_SX679_.jpg',
    link: 'https://www.amazon.com/Google-Pixel-Resistant-Smartphone-Ultrawide/dp/B08H8X23ZB/ref=sr_1_1?crid=3FWKHWR1ABI06&keywords=google+pixel+5&qid=1648053682&sprefix=google+pixel+%2Caps%2C292&sr=8-1',
    gallery: ['https://m.media-amazon.com/images/I/81-fNmQqlLL._AC_SX679_.jpg'],
    rating: 3.4,
    category: 'Google Pixel',
    NumberLikes: 0
  },
  {
    id: 12,
    name: 'Samsung Galaxy S21',
    price: 599,
    description: 'SMOOTH SCROLLING: The 120Hz display delivers a super smooth scroll, with optimized refresh rate, and a fast touch response gives seamless visuals in both work and play',
    image: 'https://m.media-amazon.com/images/I/61kLsk8RslL._AC_SX679_.jpg',
    link: 'https://www.amazon.com/Samsung-Factory-Unlocked-Smartphone-Intelligent/dp/B09BFRV59N/ref=sr_1_1?crid=2HDP5MSHTLN7S&keywords=samsung&qid=1648054001&sprefix=samsung%2Caps%2C262&sr=8-1&th=1',
    gallery: ['https://m.media-amazon.com/images/I/61kLsk8RslL._AC_SX679_.jpg'],
    rating: 2.6,
    category: 'Samsung',
    NumberLikes: 0
  }
];


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/