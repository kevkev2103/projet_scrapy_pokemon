import scrapy
from pokemonscraper.items import PokemonItem


class PokemonspiderSpider(scrapy.Spider):
    name = "pokemonspider"
    allowed_domains = ["scrapeme.live"]
    start_urls = ["https://scrapeme.live/shop/"]

    def parse(self, response):
        
        pokemons = response.css('li.product') # je viens récupérer les pokemons de la première page 
        for pokemon in pokemons:
            relative_url = pokemon.css('a').attrib['href'] # je récupère le lien pour aller sur la fiche du pokemon
            yield response.follow(relative_url,callback=self.parse_pokemon) # je clique sur le lien pour aller sur la fiche puis je fais appel a la méthode parse pokemon pour me retourner les élements définis dans cette même méthode
           
    
    def parse_pokemon(self,pokemon):
        
        pokemon_item = PokemonItem()
        pokemon_item['name']=pokemon.css('h1.product_title::text').get()#je récupère le titre
        pokemon_item['url']=pokemon.url
        pokemon_item['price']=pokemon.css('p.price span.woocommerce-Price-amount.amount::text').get()
        
        yield pokemon_item