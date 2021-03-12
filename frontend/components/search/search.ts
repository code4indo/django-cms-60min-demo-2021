import {SearchClient} from 'algoliasearch/dist/algoliasearch-lite';
import {Provide} from 'vue-property-decorator';
import {Vue, Component, Prop} from 'vue-property-decorator';
import algoliasearch from 'algoliasearch/lite';


const EaAisPagination = require('components/search/components/ea-ais-pagination.vue').default;


@Component({
    components: {
        EaAisPagination,
    }
})
export default class SearchComponent extends Vue {
    @Prop(String) algoliaApiKey: string = '';
    @Prop(String) algoliaApplicationId: string = '';
    @Prop(String) algoliaIndex: string;

    @Provide() isSearchPopupVisible: boolean = false;
    @Provide() searchClient: SearchClient = algoliasearch(this.algoliaApplicationId, this.algoliaApiKey);
    @Provide() searchQuery: string = '';
}
