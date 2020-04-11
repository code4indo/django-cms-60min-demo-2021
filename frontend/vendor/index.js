import * as Sentry from '@sentry/browser';


window.$ = window.jQuery = require("jquery");


require('bootstrap');
require('./scss/main.scss');


// Icons
require('@fortawesome/fontawesome-free/scss/fontawesome.scss');
require('@fortawesome/fontawesome-free/scss/brands.scss');
require('@fortawesome/fontawesome-free/scss/solid.scss');
require('@fortawesome/fontawesome-free/scss/regular.scss');


Sentry.init({
    dsn: '',
    environment: DJANGO.env,
});
