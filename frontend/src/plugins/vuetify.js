import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

import colors from 'vuetify/lib/util/colors'
import '@mdi/font/css/materialdesignicons.css'

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
            light: {
                //primary: colors.amber, //
                primary: colors.indigo.darken2,
                primaryVariant: colors.indigo.lighten2,
                //primaryVariant: colors.amber.lighten2,
                secondary: colors.grey.darken1,
                secondaryVariant: colors.grey.lighten3,
                background: colors.shades.white,
                surface: colors.grey.lighten2,
                error: colors.red,
                buttonBlue: colors.lightBlue.accent2,
                buttonRed: colors.red.accent1,

                onPrimary: colors.shades.white,
                onPrimaryVariant: colors.shades.white,
                onSecondary: colors.shades.white,
                onBackground: colors.grey.darken2,
                onSurface: colors.grey.darken4,
                onSurfaceVariant: colors.grey.darken2,
                onError: colors.shades.white,

            },
            dark: {
                primary: colors.blue,
                secondary: colors.grey,
            }
        },
    },
    icons: {
        iconfont: 'mdiSvg', // 'mdi' || 'mdiSvg' || 'md' || 'fa' || 'fa4' || 'faSvg'
      },
    
});
