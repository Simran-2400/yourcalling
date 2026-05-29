# YourCalling — Media Catalog
# 400 items: Books (130 EN), Movies (70 EN + 35 IT + 35 HI), Songs (55 EN + 35 IT + 40 HI)
# Tags: mood, theme, emotion — basis for cross-media similarity matching

CATALOG = [

    # ── ENGLISH BOOKS (130) ──────────────────────────────────────────────────

    {"id": "b001", "title": "The Great Gatsby", "creator": "F. Scott Fitzgerald", "media": "book", "lang": "en",
     "tags": ["longing", "obsession", "nostalgia", "illusion", "tragedy", "wealth", "decay", "romantic", "melancholic", "loss"]},

    {"id": "b002", "title": "1984", "creator": "George Orwell", "media": "book", "lang": "en",
     "tags": ["dystopia", "oppression", "fear", "surveillance", "dark", "identity", "resistance", "bleak", "power", "hopeless"]},

    {"id": "b003", "title": "To Kill a Mockingbird", "creator": "Harper Lee", "media": "book", "lang": "en",
     "tags": ["justice", "innocence", "coming-of-age", "racism", "moral", "hope", "community", "compassion", "nostalgic", "social"]},

    {"id": "b004", "title": "The Alchemist", "creator": "Paulo Coelho", "media": "book", "lang": "en",
     "tags": ["journey", "destiny", "spiritual", "hope", "adventure", "self-discovery", "inspirational", "mystical", "wonder", "faith"]},

    {"id": "b005", "title": "Pride and Prejudice", "creator": "Jane Austen", "media": "book", "lang": "en",
     "tags": ["romantic", "wit", "society", "marriage", "class", "irony", "love", "independence", "charming", "bittersweet"]},

    {"id": "b006", "title": "The Catcher in the Rye", "creator": "J.D. Salinger", "media": "book", "lang": "en",
     "tags": ["alienation", "coming-of-age", "loneliness", "rebellion", "identity", "melancholic", "introspective", "youth", "cynical", "loss"]},

    {"id": "b007", "title": "Brave New World", "creator": "Aldous Huxley", "media": "book", "lang": "en",
     "tags": ["dystopia", "control", "identity", "dark", "society", "technology", "hollow", "conformity", "bleak", "philosophical"]},

    {"id": "b008", "title": "The Road", "creator": "Cormac McCarthy", "media": "book", "lang": "en",
     "tags": ["survival", "love", "desolation", "father-son", "dark", "hope", "grief", "post-apocalyptic", "intense", "tender"]},

    {"id": "b009", "title": "One Hundred Years of Solitude", "creator": "Gabriel García Márquez", "media": "book", "lang": "en",
     "tags": ["magical", "family", "solitude", "nostalgia", "generations", "wonder", "melancholic", "epic", "mystical", "loss"]},

    {"id": "b010", "title": "Crime and Punishment", "creator": "Fyodor Dostoevsky", "media": "book", "lang": "en",
     "tags": ["guilt", "redemption", "dark", "psychological", "obsession", "moral", "suffering", "intense", "existential", "crime"]},

    {"id": "b011", "title": "The Stranger", "creator": "Albert Camus", "media": "book", "lang": "en",
     "tags": ["existential", "detachment", "alienation", "dark", "philosophical", "death", "nihilism", "cold", "introspective", "absurd"]},

    {"id": "b012", "title": "Beloved", "creator": "Toni Morrison", "media": "book", "lang": "en",
     "tags": ["grief", "trauma", "slavery", "haunting", "mother-love", "dark", "intense", "memory", "pain", "redemption"]},

    {"id": "b013", "title": "The Bell Jar", "creator": "Sylvia Plath", "media": "book", "lang": "en",
     "tags": ["depression", "identity", "feminine", "dark", "introspective", "suffering", "coming-of-age", "melancholic", "anxiety", "society"]},

    {"id": "b014", "title": "Wuthering Heights", "creator": "Emily Brontë", "media": "book", "lang": "en",
     "tags": ["obsession", "dark", "love", "revenge", "melancholic", "wild", "passionate", "haunting", "tragic", "nature"]},

    {"id": "b015", "title": "Frankenstein", "creator": "Mary Shelley", "media": "book", "lang": "en",
     "tags": ["creation", "loneliness", "dark", "science", "rejection", "tragic", "gothic", "identity", "fear", "moral"]},

    {"id": "b016", "title": "Moby Dick", "creator": "Herman Melville", "media": "book", "lang": "en",
     "tags": ["obsession", "adventure", "sea", "dark", "epic", "fate", "destruction", "intense", "nature", "philosophical"]},

    {"id": "b017", "title": "Jane Eyre", "creator": "Charlotte Brontë", "media": "book", "lang": "en",
     "tags": ["love", "independence", "gothic", "identity", "resilience", "bittersweet", "romantic", "class", "moral", "passionate"]},

    {"id": "b018", "title": "The Count of Monte Cristo", "creator": "Alexandre Dumas", "media": "book", "lang": "en",
     "tags": ["revenge", "justice", "adventure", "transformation", "betrayal", "triumph", "epic", "romantic", "cunning", "resilience"]},

    {"id": "b019", "title": "Anna Karenina", "creator": "Leo Tolstoy", "media": "book", "lang": "en",
     "tags": ["tragic", "love", "society", "obsession", "passion", "melancholic", "moral", "class", "feminine", "suffocation"]},

    {"id": "b020", "title": "The Picture of Dorian Gray", "creator": "Oscar Wilde", "media": "book", "lang": "en",
     "tags": ["vanity", "dark", "corruption", "beauty", "obsession", "gothic", "moral", "decadence", "tragic", "art"]},

    {"id": "b021", "title": "Slaughterhouse-Five", "creator": "Kurt Vonnegut", "media": "book", "lang": "en",
     "tags": ["war", "trauma", "dark", "absurd", "time", "grief", "satirical", "surreal", "anti-war", "bleak"]},

    {"id": "b022", "title": "The Old Man and the Sea", "creator": "Ernest Hemingway", "media": "book", "lang": "en",
     "tags": ["solitude", "perseverance", "nature", "defeat", "dignity", "peaceful", "bittersweet", "minimalist", "sea", "aging"]},

    {"id": "b023", "title": "Lolita", "creator": "Vladimir Nabokov", "media": "book", "lang": "en",
     "tags": ["obsession", "dark", "disturbing", "beauty", "unreliable", "tragic", "complex", "controversial", "melancholic", "manipulation"]},

    {"id": "b024", "title": "On the Road", "creator": "Jack Kerouac", "media": "book", "lang": "en",
     "tags": ["freedom", "adventure", "youth", "restless", "friendship", "rebellious", "jazz", "America", "searching", "energetic"]},

    {"id": "b025", "title": "Catch-22", "creator": "Joseph Heller", "media": "book", "lang": "en",
     "tags": ["war", "satirical", "dark", "absurd", "bureaucracy", "survival", "comedic", "cynical", "bleak", "irony"]},

    {"id": "b026", "title": "The Hitchhiker's Guide to the Galaxy", "creator": "Douglas Adams", "media": "book", "lang": "en",
     "tags": ["comedic", "absurd", "space", "whimsical", "satirical", "adventure", "philosophical", "fun", "irony", "wonder"]},

    {"id": "b027", "title": "Harry Potter and the Sorcerer's Stone", "creator": "J.K. Rowling", "media": "book", "lang": "en",
     "tags": ["magic", "friendship", "wonder", "coming-of-age", "adventure", "good-vs-evil", "hope", "joyful", "whimsical", "belonging"]},

    {"id": "b028", "title": "The Lord of the Rings", "creator": "J.R.R. Tolkien", "media": "book", "lang": "en",
     "tags": ["epic", "adventure", "friendship", "good-vs-evil", "hope", "sacrifice", "wonder", "journey", "courage", "mythic"]},

    {"id": "b029", "title": "Dune", "creator": "Frank Herbert", "media": "book", "lang": "en",
     "tags": ["epic", "power", "desert", "destiny", "political", "mystical", "survival", "transformation", "dark", "philosophical"]},

    {"id": "b030", "title": "The Handmaid's Tale", "creator": "Margaret Atwood", "media": "book", "lang": "en",
     "tags": ["dystopia", "oppression", "feminine", "dark", "resistance", "trauma", "fear", "society", "political", "suffocation"]},

    {"id": "b031", "title": "Invisible Man", "creator": "Ralph Ellison", "media": "book", "lang": "en",
     "tags": ["identity", "race", "invisibility", "society", "alienation", "dark", "searching", "anger", "injustice", "introspective"]},

    {"id": "b032", "title": "Siddhartha", "creator": "Hermann Hesse", "media": "book", "lang": "en",
     "tags": ["spiritual", "journey", "self-discovery", "peaceful", "philosophical", "enlightenment", "introspective", "faith", "wisdom", "serene"]},

    {"id": "b033", "title": "The Brothers Karamazov", "creator": "Fyodor Dostoevsky", "media": "book", "lang": "en",
     "tags": ["family", "faith", "doubt", "dark", "moral", "intense", "philosophical", "suffering", "redemption", "complex"]},

    {"id": "b034", "title": "A Tale of Two Cities", "creator": "Charles Dickens", "media": "book", "lang": "en",
     "tags": ["sacrifice", "revolution", "love", "historical", "dark", "redemption", "epic", "social", "tragic", "heroic"]},

    {"id": "b035", "title": "Midnight's Children", "creator": "Salman Rushdie", "media": "book", "lang": "en",
     "tags": ["magical", "historical", "India", "identity", "epic", "satirical", "wonder", "complex", "political", "memory"]},

    {"id": "b036", "title": "Things Fall Apart", "creator": "Chinua Achebe", "media": "book", "lang": "en",
     "tags": ["tragic", "culture", "colonialism", "pride", "loss", "family", "dark", "tradition", "identity", "grief"]},

    {"id": "b037", "title": "The Kite Runner", "creator": "Khaled Hosseini", "media": "book", "lang": "en",
     "tags": ["guilt", "redemption", "friendship", "war", "grief", "love", "betrayal", "bittersweet", "Afghanistan", "hope"]},

    {"id": "b038", "title": "A Thousand Splendid Suns", "creator": "Khaled Hosseini", "media": "book", "lang": "en",
     "tags": ["resilience", "feminine", "war", "love", "suffering", "hope", "bittersweet", "dark", "Afghanistan", "sacrifice"]},

    {"id": "b039", "title": "The House on Mango Street", "creator": "Sandra Cisneros", "media": "book", "lang": "en",
     "tags": ["coming-of-age", "identity", "community", "longing", "bittersweet", "feminine", "lyrical", "poverty", "dreams", "nostalgic"]},

    {"id": "b040", "title": "Their Eyes Were Watching God", "creator": "Zora Neale Hurston", "media": "book", "lang": "en",
     "tags": ["love", "identity", "freedom", "feminine", "passionate", "resilience", "community", "joyful", "bittersweet", "coming-of-age"]},

    {"id": "b041", "title": "Flowers for Algernon", "creator": "Daniel Keyes", "media": "book", "lang": "en",
     "tags": ["intelligence", "identity", "tragic", "loneliness", "dark", "science", "bittersweet", "emotional", "transformation", "loss"]},

    {"id": "b042", "title": "The Color Purple", "creator": "Alice Walker", "media": "book", "lang": "en",
     "tags": ["resilience", "feminine", "trauma", "love", "hope", "dark", "community", "redemption", "spiritual", "triumph"]},

    {"id": "b043", "title": "Ender's Game", "creator": "Orson Scott Card", "media": "book", "lang": "en",
     "tags": ["identity", "war", "genius", "isolation", "dark", "moral", "science-fiction", "coming-of-age", "strategy", "sacrifice"]},

    {"id": "b044", "title": "The Giver", "creator": "Lois Lowry", "media": "book", "lang": "en",
     "tags": ["dystopia", "memory", "loss", "coming-of-age", "dark", "hope", "society", "conformity", "bittersweet", "awakening"]},

    {"id": "b045", "title": "Of Mice and Men", "creator": "John Steinbeck", "media": "book", "lang": "en",
     "tags": ["friendship", "dreams", "tragic", "poverty", "loneliness", "bittersweet", "dark", "sacrifice", "loss", "America"]},

    {"id": "b046", "title": "East of Eden", "creator": "John Steinbeck", "media": "book", "lang": "en",
     "tags": ["good-vs-evil", "family", "epic", "moral", "identity", "America", "dark", "redemption", "generational", "complex"]},

    {"id": "b047", "title": "The Sun Also Rises", "creator": "Ernest Hemingway", "media": "book", "lang": "en",
     "tags": ["disillusion", "loss", "romantic", "dark", "melancholic", "post-war", "searching", "friendship", "drinking", "nostalgia"]},

    {"id": "b048", "title": "Invisible Cities", "creator": "Italo Calvino", "media": "book", "lang": "en",
     "tags": ["wonder", "imagination", "lyrical", "philosophical", "surreal", "memory", "dreamy", "poetic", "introspective", "mystical"]},

    {"id": "b049", "title": "Never Let Me Go", "creator": "Kazuo Ishiguro", "media": "book", "lang": "en",
     "tags": ["melancholic", "memory", "loss", "identity", "dark", "bittersweet", "dystopia", "love", "tragic", "resigned"]},

    {"id": "b050", "title": "The Remains of the Day", "creator": "Kazuo Ishiguro", "media": "book", "lang": "en",
     "tags": ["regret", "memory", "repression", "melancholic", "duty", "love-lost", "bittersweet", "quiet", "introspective", "dignity"]},

    {"id": "b051", "title": "Shantaram", "creator": "Gregory David Roberts", "media": "book", "lang": "en",
     "tags": ["adventure", "India", "redemption", "friendship", "dark", "freedom", "epic", "gritty", "spiritual", "intense"]},

    {"id": "b052", "title": "The Shadow of the Wind", "creator": "Carlos Ruiz Zafón", "media": "book", "lang": "en",
     "tags": ["mystery", "dark", "books", "nostalgia", "gothic", "Spain", "romantic", "intrigue", "haunting", "passion"]},

    {"id": "b053", "title": "Norwegian Wood", "creator": "Haruki Murakami", "media": "book", "lang": "en",
     "tags": ["love", "grief", "melancholic", "nostalgia", "youth", "loss", "bittersweet", "quiet", "introspective", "longing"]},

    {"id": "b054", "title": "Kafka on the Shore", "creator": "Haruki Murakami", "media": "book", "lang": "en",
     "tags": ["surreal", "mystical", "searching", "identity", "dark", "magical", "dreamy", "adventure", "fate", "wonder"]},

    {"id": "b055", "title": "The Wind-Up Bird Chronicle", "creator": "Haruki Murakami", "media": "book", "lang": "en",
     "tags": ["surreal", "dark", "searching", "identity", "war", "mystery", "quiet", "dreamy", "sinister", "introspective"]},

    {"id": "b056", "title": "The Name of the Rose", "creator": "Umberto Eco", "media": "book", "lang": "en",
     "tags": ["mystery", "dark", "medieval", "intellectual", "religion", "intrigue", "gothic", "suspense", "detective", "philosophical"]},

    {"id": "b057", "title": "Love in the Time of Cholera", "creator": "Gabriel García Márquez", "media": "book", "lang": "en",
     "tags": ["love", "longing", "patience", "romantic", "bittersweet", "magical", "obsession", "aging", "passion", "tropical"]},

    {"id": "b058", "title": "The Brief Wondrous Life of Oscar Wao", "creator": "Junot Díaz", "media": "book", "lang": "en",
     "tags": ["identity", "love", "dark", "diaspora", "family", "tragedy", "culture", "geek", "passionate", "Dominican"]},

    {"id": "b059", "title": "Life of Pi", "creator": "Yann Martel", "media": "book", "lang": "en",
     "tags": ["survival", "spiritual", "wonder", "animal", "sea", "faith", "philosophical", "magical", "isolation", "hope"]},

    {"id": "b060", "title": "The Secret Garden", "creator": "Frances Hodgson Burnett", "media": "book", "lang": "en",
     "tags": ["healing", "nature", "hope", "wonder", "childhood", "transformation", "joyful", "whimsical", "friendship", "rebirth"]},

    {"id": "b061", "title": "Rebecca", "creator": "Daphne du Maurier", "media": "book", "lang": "en",
     "tags": ["gothic", "dark", "obsession", "suspense", "haunting", "romantic", "jealousy", "mystery", "psychological", "fear"]},

    {"id": "b062", "title": "Gone with the Wind", "creator": "Margaret Mitchell", "media": "book", "lang": "en",
     "tags": ["epic", "romantic", "war", "survival", "tragedy", "passion", "America", "nostalgia", "resilience", "historical"]},

    {"id": "b063", "title": "A Farewell to Arms", "creator": "Ernest Hemingway", "media": "book", "lang": "en",
     "tags": ["war", "love", "tragic", "loss", "dark", "melancholic", "romantic", "grief", "disillusion", "sacrifice"]},

    {"id": "b064", "title": "For Whom the Bell Tolls", "creator": "Ernest Hemingway", "media": "book", "lang": "en",
     "tags": ["war", "sacrifice", "love", "dark", "courage", "tragic", "political", "intense", "death", "honor"]},

    {"id": "b065", "title": "The Grapes of Wrath", "creator": "John Steinbeck", "media": "book", "lang": "en",
     "tags": ["poverty", "resilience", "family", "America", "dark", "social", "struggle", "hope", "epic", "loss"]},

    {"id": "b066", "title": "Fahrenheit 451", "creator": "Ray Bradbury", "media": "book", "lang": "en",
     "tags": ["dystopia", "censorship", "awakening", "dark", "books", "conformity", "resistance", "identity", "bleak", "hope"]},

    {"id": "b067", "title": "Neuromancer", "creator": "William Gibson", "media": "book", "lang": "en",
     "tags": ["cyberpunk", "dark", "technology", "noir", "addiction", "crime", "dystopia", "fast", "identity", "gritty"]},

    {"id": "b068", "title": "Solaris", "creator": "Stanisław Lem", "media": "book", "lang": "en",
     "tags": ["philosophical", "science-fiction", "mystery", "isolation", "dark", "alien", "introspective", "grief", "surreal", "wonder"]},

    {"id": "b069", "title": "The Master and Margarita", "creator": "Mikhail Bulgakov", "media": "book", "lang": "en",
     "tags": ["dark", "satirical", "magic", "surreal", "Soviet", "comedic", "philosophical", "evil", "love", "provocative"]},

    {"id": "b070", "title": "Atlas Shrugged", "creator": "Ayn Rand", "media": "book", "lang": "en",
     "tags": ["ambition", "philosophical", "society", "intellectual", "dark", "political", "identity", "controversial", "epic", "independence"]},

    {"id": "b071", "title": "The Trial", "creator": "Franz Kafka", "media": "book", "lang": "en",
     "tags": ["absurd", "dark", "bureaucracy", "anxiety", "existential", "helpless", "surreal", "oppression", "fear", "bleak"]},

    {"id": "b072", "title": "Death of a Salesman", "creator": "Arthur Miller", "media": "book", "lang": "en",
     "tags": ["tragic", "failure", "America", "dreams", "dark", "family", "loss", "disillusion", "identity", "melancholic"]},

    {"id": "b073", "title": "The Outsiders", "creator": "S.E. Hinton", "media": "book", "lang": "en",
     "tags": ["coming-of-age", "friendship", "loyalty", "violence", "class", "dark", "bittersweet", "youth", "belonging", "tragic"]},

    {"id": "b074", "title": "The Perks of Being a Wallflower", "creator": "Stephen Chbosky", "media": "book", "lang": "en",
     "tags": ["coming-of-age", "trauma", "friendship", "bittersweet", "emotional", "nostalgia", "mental-health", "love", "youth", "melancholic"]},

    {"id": "b075", "title": "The Curious Incident of the Dog in the Night-Time", "creator": "Mark Haddon", "media": "book", "lang": "en",
     "tags": ["neurodiversity", "mystery", "identity", "family", "bittersweet", "dark", "introspective", "unique", "truth", "coming-of-age"]},

    {"id": "b076", "title": "Educated", "creator": "Tara Westover", "media": "book", "lang": "en",
     "tags": ["resilience", "memoir", "education", "family", "dark", "trauma", "identity", "hope", "transformation", "freedom"]},

    {"id": "b077", "title": "Sapiens", "creator": "Yuval Noah Harari", "media": "book", "lang": "en",
     "tags": ["history", "intellectual", "humanity", "philosophical", "wonder", "civilization", "power", "science", "thought-provoking", "epic"]},

    {"id": "b078", "title": "The Subtle Art of Not Giving a F*ck", "creator": "Mark Manson", "media": "book", "lang": "en",
     "tags": ["self-help", "rebellious", "pragmatic", "humorous", "honest", "identity", "freedom", "counterintuitive", "direct", "modern"]},

    {"id": "b079", "title": "Thinking Fast and Slow", "creator": "Daniel Kahneman", "media": "book", "lang": "en",
     "tags": ["psychology", "intellectual", "decision-making", "wonder", "scientific", "human-nature", "thoughtful", "insight", "rational", "complex"]},

    {"id": "b080", "title": "The Power of Now", "creator": "Eckhart Tolle", "media": "book", "lang": "en",
     "tags": ["spiritual", "peaceful", "mindfulness", "serene", "introspective", "enlightenment", "present", "healing", "philosophical", "calm"]},

    {"id": "b081", "title": "Man's Search for Meaning", "creator": "Viktor Frankl", "media": "book", "lang": "en",
     "tags": ["meaning", "suffering", "hope", "dark", "philosophical", "resilience", "Holocaust", "spiritual", "profound", "inspiring"]},

    {"id": "b082", "title": "The Diary of a Young Girl", "creator": "Anne Frank", "media": "book", "lang": "en",
     "tags": ["hope", "dark", "war", "survival", "youth", "tragic", "courage", "memoir", "historical", "bittersweet"]},

    {"id": "b083", "title": "Night", "creator": "Elie Wiesel", "media": "book", "lang": "en",
     "tags": ["dark", "Holocaust", "survival", "faith-lost", "grief", "horrific", "father-son", "memoir", "tragic", "bearing-witness"]},

    {"id": "b084", "title": "The God of Small Things", "creator": "Arundhati Roy", "media": "book", "lang": "en",
     "tags": ["tragic", "India", "love", "caste", "dark", "family", "lyrical", "forbidden", "grief", "beautiful"]},

    {"id": "b085", "title": "Interpreter of Maladies", "creator": "Jhumpa Lahiri", "media": "book", "lang": "en",
     "tags": ["diaspora", "loneliness", "bittersweet", "identity", "cultural", "relationships", "quiet", "melancholic", "India", "longing"]},

    {"id": "b086", "title": "White Teeth", "creator": "Zadie Smith", "media": "book", "lang": "en",
     "tags": ["identity", "multicultural", "satirical", "family", "England", "humorous", "society", "complex", "generational", "modern"]},

    {"id": "b087", "title": "The Road Back to You", "creator": "Ian Morgan Cron", "media": "book", "lang": "en",
     "tags": ["self-discovery", "spiritual", "personality", "introspective", "thoughtful", "identity", "healing", "growth", "honest", "practical"]},

    {"id": "b088", "title": "The Midnight Library", "creator": "Matt Haig", "media": "book", "lang": "en",
     "tags": ["hope", "regret", "choice", "bittersweet", "life", "depression", "wonder", "healing", "redemption", "emotional"]},

    {"id": "b089", "title": "Eleanor Oliphant Is Completely Fine", "creator": "Gail Honeyman", "media": "book", "lang": "en",
     "tags": ["loneliness", "healing", "dark", "bittersweet", "identity", "trauma", "friendship", "hope", "transformation", "quirky"]},

    {"id": "b090", "title": "Where the Crawdads Sing", "creator": "Delia Owens", "media": "book", "lang": "en",
     "tags": ["nature", "loneliness", "resilience", "mystery", "bittersweet", "love", "survival", "coming-of-age", "beautiful", "grief"]},

    {"id": "b091", "title": "The Night Circus", "creator": "Erin Morgenstern", "media": "book", "lang": "en",
     "tags": ["magical", "wonder", "romantic", "dark", "dreamy", "love", "competition", "enchanting", "whimsical", "atmospheric"]},

    {"id": "b092", "title": "Station Eleven", "creator": "Emily St. John Mandel", "media": "book", "lang": "en",
     "tags": ["post-apocalyptic", "hope", "art", "survival", "memory", "bittersweet", "civilization", "connection", "dark", "literary"]},

    {"id": "b093", "title": "All the Light We Cannot See", "creator": "Anthony Doerr", "media": "book", "lang": "en",
     "tags": ["war", "hope", "dark", "bittersweet", "love", "science", "historical", "lyrical", "tragic", "wonder"]},

    {"id": "b094", "title": "The Shadow of the Wind", "creator": "Carlos Ruiz Zafón", "media": "book", "lang": "en",
     "tags": ["mystery", "dark", "books", "nostalgia", "gothic", "Spain", "romantic", "intrigue", "haunting", "passion"]},

    {"id": "b095", "title": "Pachinko", "creator": "Min Jin Lee", "media": "book", "lang": "en",
     "tags": ["generational", "identity", "discrimination", "Korea", "dark", "family", "resilience", "sacrifice", "epic", "longing"]},

    {"id": "b096", "title": "Lincoln in the Bardo", "creator": "George Saunders", "media": "book", "lang": "en",
     "tags": ["grief", "death", "dark", "surreal", "philosophical", "love", "historical", "bittersweet", "haunting", "unique"]},

    {"id": "b097", "title": "A Gentleman in Moscow", "creator": "Amor Towles", "media": "book", "lang": "en",
     "tags": ["elegant", "nostalgic", "charming", "hope", "history", "Russia", "wit", "philosophical", "bittersweet", "civilized"]},

    {"id": "b098", "title": "The Power", "creator": "Naomi Alderman", "media": "book", "lang": "en",
     "tags": ["power", "gender", "dark", "dystopia", "satirical", "society", "provocative", "feminist", "political", "intense"]},

    {"id": "b099", "title": "Piranesi", "creator": "Susanna Clarke", "media": "book", "lang": "en",
     "tags": ["wonder", "mystery", "surreal", "dreamy", "philosophical", "identity", "magical", "enchanting", "unique", "dark"]},

    {"id": "b100", "title": "Circe", "creator": "Madeline Miller", "media": "book", "lang": "en",
     "tags": ["mythological", "feminine", "power", "magical", "identity", "dark", "transformation", "resilience", "wonder", "passionate"]},

    {"id": "b101", "title": "The Song of Achilles", "creator": "Madeline Miller", "media": "book", "lang": "en",
     "tags": ["love", "mythological", "tragic", "war", "passionate", "bittersweet", "loyalty", "beauty", "heroic", "loss"]},

    {"id": "b102", "title": "Project Hail Mary", "creator": "Andy Weir", "media": "book", "lang": "en",
     "tags": ["adventure", "science", "hope", "friendship", "space", "survival", "wonder", "smart", "heartwarming", "optimistic"]},

    {"id": "b103", "title": "The Martian", "creator": "Andy Weir", "media": "book", "lang": "en",
     "tags": ["survival", "science", "humorous", "hope", "space", "resilience", "optimistic", "problem-solving", "tense", "witty"]},

    {"id": "b104", "title": "The Three-Body Problem", "creator": "Liu Cixin", "media": "book", "lang": "en",
     "tags": ["science-fiction", "dark", "intellectual", "philosophical", "epic", "alien", "complex", "historical", "wonder", "cold"]},

    {"id": "b105", "title": "The Pillars of the Earth", "creator": "Ken Follett", "media": "book", "lang": "en",
     "tags": ["historical", "epic", "dark", "cathedral", "medieval", "power", "love", "resilience", "complex", "sweeping"]},

    {"id": "b106", "title": "Shogun", "creator": "James Clavell", "media": "book", "lang": "en",
     "tags": ["historical", "Japan", "adventure", "cultural", "power", "honor", "epic", "dark", "fascinating", "clash-of-cultures"]},

    {"id": "b107", "title": "Cloud Atlas", "creator": "David Mitchell", "media": "book", "lang": "en",
     "tags": ["epic", "philosophical", "reincarnation", "dark", "hope", "complex", "interconnected", "time", "humanity", "literary"]},

    {"id": "b108", "title": "If on a Winter's Night a Traveler", "creator": "Italo Calvino", "media": "book", "lang": "en",
     "tags": ["meta", "playful", "books", "surreal", "witty", "philosophical", "unique", "experimental", "identity", "clever"]},

    {"id": "b109", "title": "The English Patient", "creator": "Michael Ondaatje", "media": "book", "lang": "en",
     "tags": ["war", "love", "lyrical", "dark", "bittersweet", "memory", "identity", "beautiful", "tragic", "fragmented"]},

    {"id": "b110", "title": "The Poisonwood Bible", "creator": "Barbara Kingsolver", "media": "book", "lang": "en",
     "tags": ["Africa", "family", "dark", "colonialism", "faith", "feminine", "tragic", "complex", "guilt", "political"]},

    {"id": "b111", "title": "Wolf Hall", "creator": "Hilary Mantel", "media": "book", "lang": "en",
     "tags": ["historical", "power", "dark", "political", "Tudor", "cunning", "psychological", "intrigue", "complex", "brilliant"]},

    {"id": "b112", "title": "Birdsong", "creator": "Sebastian Faulks", "media": "book", "lang": "en",
     "tags": ["war", "love", "dark", "tragic", "historical", "WWI", "bittersweet", "sacrifice", "intense", "profound"]},

    {"id": "b113", "title": "The Hours", "creator": "Michael Cunningham", "media": "book", "lang": "en",
     "tags": ["feminine", "dark", "depression", "literary", "time", "bittersweet", "introspective", "death", "quiet", "lyrical"]},

    {"id": "b114", "title": "Beloved", "creator": "Toni Morrison", "media": "book", "lang": "en",
     "tags": ["grief", "slavery", "dark", "haunting", "trauma", "love", "freedom", "African-American", "intense", "redemption"]},

    {"id": "b115", "title": "The House of the Spirits", "creator": "Isabel Allende", "media": "book", "lang": "en",
     "tags": ["magical", "family", "political", "dark", "feminine", "generations", "Latin-America", "love", "resilience", "haunting"]},

    {"id": "b116", "title": "Americanah", "creator": "Chimamanda Ngozi Adichie", "media": "book", "lang": "en",
     "tags": ["race", "identity", "love", "diaspora", "modern", "Nigeria", "feminist", "bittersweet", "searching", "insightful"]},

    {"id": "b117", "title": "Purple Hibiscus", "creator": "Chimamanda Ngozi Adichie", "media": "book", "lang": "en",
     "tags": ["family", "religion", "dark", "trauma", "coming-of-age", "Nigeria", "silent-suffering", "hope", "bittersweet", "complex"]},

    {"id": "b118", "title": "The Famished Road", "creator": "Ben Okri", "media": "book", "lang": "en",
     "tags": ["magical", "spiritual", "Nigeria", "dark", "childhood", "spirit-world", "bittersweet", "lyrical", "mystical", "wonder"]},

    {"id": "b119", "title": "Half of a Yellow Sun", "creator": "Chimamanda Ngozi Adichie", "media": "book", "lang": "en",
     "tags": ["war", "love", "dark", "Nigeria", "historical", "tragic", "survival", "political", "family", "intense"]},

    {"id": "b120", "title": "The White Tiger", "creator": "Aravind Adiga", "media": "book", "lang": "en",
     "tags": ["dark", "India", "class", "ambition", "crime", "satirical", "anger", "gritty", "freedom", "provocative"]},

    {"id": "b121", "title": "The Space Between Us", "creator": "Thrity Umrigar", "media": "book", "lang": "en",
     "tags": ["class", "India", "friendship", "bittersweet", "dark", "feminine", "social", "complex", "quiet", "emotional"]},

    {"id": "b122", "title": "A Fine Balance", "creator": "Rohinton Mistry", "media": "book", "lang": "en",
     "tags": ["dark", "India", "tragedy", "resilience", "poverty", "friendship", "political", "suffering", "human-spirit", "profound"]},

    {"id": "b123", "title": "The Inheritance Games", "creator": "Jennifer Lynn Barnes", "media": "book", "lang": "en",
     "tags": ["mystery", "puzzle", "romance", "thrilling", "fun", "clever", "suspense", "wealthy", "game", "fast-paced"]},

    {"id": "b124", "title": "Six of Crows", "creator": "Leigh Bardugo", "media": "book", "lang": "en",
     "tags": ["heist", "dark", "adventure", "clever", "friendship", "fantasy", "morally-grey", "tension", "wit", "ensemble"]},

    {"id": "b125", "title": "The Invisible Life of Addie LaRue", "creator": "V.E. Schwab", "media": "book", "lang": "en",
     "tags": ["magical", "bittersweet", "love", "dark", "loneliness", "identity", "memory", "wonder", "romantic", "longing"]},

    {"id": "b126", "title": "Anxious People", "creator": "Fredrik Backman", "media": "book", "lang": "en",
     "tags": ["humorous", "bittersweet", "connection", "dark", "hopeful", "ensemble", "witty", "touching", "anxiety", "human-nature"]},

    {"id": "b127", "title": "A Man Called Ove", "creator": "Fredrik Backman", "media": "book", "lang": "en",
     "tags": ["heartwarming", "bittersweet", "grief", "community", "humor", "love-lost", "touching", "dark", "redemption", "connection"]},

    {"id": "b128", "title": "The Little Prince", "creator": "Antoine de Saint-Exupéry", "media": "book", "lang": "en",
     "tags": ["wonder", "philosophical", "bittersweet", "childhood", "love", "innocent", "profound", "lyrical", "whimsical", "melancholic"]},

    {"id": "b129", "title": "Jonathan Livingston Seagull", "creator": "Richard Bach", "media": "book", "lang": "en",
     "tags": ["spiritual", "freedom", "inspirational", "wonder", "self-discovery", "philosophical", "simple", "soaring", "hope", "transcendent"]},

    {"id": "b130", "title": "Tuesdays with Morrie", "creator": "Mitch Albom", "media": "book", "lang": "en",
     "tags": ["wisdom", "death", "love", "bittersweet", "friendship", "hopeful", "touching", "grief", "meaning", "philosophical"]},

    # ── ENGLISH MOVIES (70) ──────────────────────────────────────────────────

    {"id": "m001", "title": "The Shawshank Redemption", "creator": "Frank Darabont", "media": "movie", "lang": "en",
     "tags": ["hope", "friendship", "resilience", "dark", "redemption", "triumph", "prison", "inspiring", "bittersweet", "justice"]},

    {"id": "m002", "title": "The Godfather", "creator": "Francis Ford Coppola", "media": "movie", "lang": "en",
     "tags": ["power", "family", "dark", "crime", "tragedy", "loyalty", "corruption", "epic", "honor", "complex"]},

    {"id": "m003", "title": "Inception", "creator": "Christopher Nolan", "media": "movie", "lang": "en",
     "tags": ["mind-bending", "surreal", "dark", "grief", "adventure", "clever", "identity", "dreamy", "obsession", "tense"]},

    {"id": "m004", "title": "Interstellar", "creator": "Christopher Nolan", "media": "movie", "lang": "en",
     "tags": ["space", "love", "dark", "epic", "wonder", "science", "sacrifice", "philosophical", "emotional", "hope"]},

    {"id": "m005", "title": "Eternal Sunshine of the Spotless Mind", "creator": "Michel Gondry", "media": "movie", "lang": "en",
     "tags": ["love", "memory", "melancholic", "romantic", "surreal", "bittersweet", "loss", "dreamy", "longing", "grief"]},

    {"id": "m006", "title": "Her", "creator": "Spike Jonze", "media": "movie", "lang": "en",
     "tags": ["love", "loneliness", "technology", "melancholic", "identity", "bittersweet", "modern", "beautiful", "philosophical", "longing"]},

    {"id": "m007", "title": "Blade Runner 2049", "creator": "Denis Villeneuve", "media": "movie", "lang": "en",
     "tags": ["identity", "dark", "dystopia", "lonely", "philosophical", "cinematic", "bleak", "search", "wonder", "melancholic"]},

    {"id": "m008", "title": "2001: A Space Odyssey", "creator": "Stanley Kubrick", "media": "movie", "lang": "en",
     "tags": ["wonder", "philosophical", "space", "cold", "mysterious", "epic", "surreal", "dark", "humanity", "transcendent"]},

    {"id": "m009", "title": "Whiplash", "creator": "Damien Chazelle", "media": "movie", "lang": "en",
     "tags": ["obsession", "ambition", "dark", "music", "intense", "tense", "perfectionism", "driven", "complex", "passionate"]},

    {"id": "m010", "title": "The Truman Show", "creator": "Peter Weir", "media": "movie", "lang": "en",
     "tags": ["identity", "reality", "dark", "philosophical", "satirical", "hope", "freedom", "bittersweet", "awakening", "society"]},

    {"id": "m011", "title": "Schindler's List", "creator": "Steven Spielberg", "media": "movie", "lang": "en",
     "tags": ["war", "dark", "hope", "redemption", "Holocaust", "tragic", "humanity", "sacrifice", "profound", "historical"]},

    {"id": "m012", "title": "Saving Private Ryan", "creator": "Steven Spielberg", "media": "movie", "lang": "en",
     "tags": ["war", "dark", "sacrifice", "brotherhood", "tragedy", "intense", "heroic", "loss", "honor", "WWII"]},

    {"id": "m013", "title": "Apocalypse Now", "creator": "Francis Ford Coppola", "media": "movie", "lang": "en",
     "tags": ["war", "dark", "obsession", "madness", "psychological", "intense", "dark", "surreal", "philosophical", "Vietnam"]},

    {"id": "m014", "title": "Full Metal Jacket", "creator": "Stanley Kubrick", "media": "movie", "lang": "en",
     "tags": ["war", "dark", "trauma", "dehumanization", "bleak", "satirical", "intense", "military", "complex", "Vietnam"]},

    {"id": "m015", "title": "Forrest Gump", "creator": "Robert Zemeckis", "media": "movie", "lang": "en",
     "tags": ["hope", "love", "nostalgia", "bittersweet", "inspirational", "America", "history", "heartwarming", "loss", "journey"]},

    {"id": "m016", "title": "Good Will Hunting", "creator": "Gus Van Sant", "media": "movie", "lang": "en",
     "tags": ["genius", "trauma", "friendship", "love", "dark", "bittersweet", "healing", "identity", "hope", "emotional"]},

    {"id": "m017", "title": "Dead Poets Society", "creator": "Peter Weir", "media": "movie", "lang": "en",
     "tags": ["inspirational", "coming-of-age", "poetry", "dark", "tragic", "conformity", "freedom", "rebellion", "bittersweet", "friendship"]},

    {"id": "m018", "title": "The Breakfast Club", "creator": "John Hughes", "media": "movie", "lang": "en",
     "tags": ["coming-of-age", "identity", "youth", "friendship", "rebellion", "bittersweet", "nostalgia", "society", "fun", "connection"]},

    {"id": "m019", "title": "Ferris Bueller's Day Off", "creator": "John Hughes", "media": "movie", "lang": "en",
     "tags": ["freedom", "youth", "comedic", "fun", "rebellious", "nostalgic", "friendship", "adventure", "carefree", "joyful"]},

    {"id": "m020", "title": "The Dark Knight", "creator": "Christopher Nolan", "media": "movie", "lang": "en",
     "tags": ["dark", "philosophical", "chaos", "heroic", "complex", "moral", "tense", "intense", "brilliant", "iconic"]},

    {"id": "m021", "title": "Fight Club", "creator": "David Fincher", "media": "movie", "lang": "en",
     "tags": ["dark", "identity", "rebellion", "psychological", "twist", "intense", "anarchist", "provocative", "disillusion", "masculine"]},

    {"id": "m022", "title": "American Beauty", "creator": "Sam Mendes", "media": "movie", "lang": "en",
     "tags": ["dark", "suburban", "disillusion", "beauty", "identity", "satirical", "melancholic", "bittersweet", "awakening", "tragic"]},

    {"id": "m023", "title": "Lost in Translation", "creator": "Sofia Coppola", "media": "movie", "lang": "en",
     "tags": ["loneliness", "connection", "bittersweet", "quiet", "melancholic", "Japan", "love-almost", "nostalgic", "beautiful", "searching"]},

    {"id": "m024", "title": "Before Sunrise", "creator": "Richard Linklater", "media": "movie", "lang": "en",
     "tags": ["romantic", "bittersweet", "youth", "philosophical", "connection", "love", "fleeting", "beautiful", "nostalgic", "hope"]},

    {"id": "m025", "title": "Moonlight", "creator": "Barry Jenkins", "media": "movie", "lang": "en",
     "tags": ["identity", "love", "dark", "bittersweet", "coming-of-age", "tender", "poetic", "loneliness", "beautiful", "quiet"]},

    {"id": "m026", "title": "La La Land", "creator": "Damien Chazelle", "media": "movie", "lang": "en",
     "tags": ["romantic", "dreams", "music", "bittersweet", "love", "nostalgia", "hope", "loss", "beautiful", "melancholic"]},

    {"id": "m027", "title": "Parasite", "creator": "Bong Joon-ho", "media": "movie", "lang": "en",
     "tags": ["class", "dark", "satirical", "twist", "clever", "family", "social", "tense", "dark-comedy", "provocative"]},

    {"id": "m028", "title": "The Social Network", "creator": "David Fincher", "media": "movie", "lang": "en",
     "tags": ["ambition", "betrayal", "modern", "dark", "clever", "wealth", "loneliness", "fast-paced", "driven", "complex"]},

    {"id": "m029", "title": "There Will Be Blood", "creator": "Paul Thomas Anderson", "media": "movie", "lang": "en",
     "tags": ["obsession", "greed", "dark", "power", "ambition", "epic", "intense", "tragic", "America", "isolation"]},

    {"id": "m030", "title": "No Country for Old Men", "creator": "Coen Brothers", "media": "movie", "lang": "en",
     "tags": ["dark", "evil", "bleak", "fate", "suspense", "violent", "philosophical", "tense", "nihilism", "America"]},

    {"id": "m031", "title": "Arrival", "creator": "Denis Villeneuve", "media": "movie", "lang": "en",
     "tags": ["wonder", "love", "grief", "philosophical", "alien", "time", "bittersweet", "beautiful", "science", "emotional"]},

    {"id": "m032", "title": "Gravity", "creator": "Alfonso Cuarón", "media": "movie", "lang": "en",
     "tags": ["survival", "space", "hope", "grief", "tense", "beautiful", "intense", "redemption", "isolation", "rebirth"]},

    {"id": "m033", "title": "The Revenant", "creator": "Alejandro González Iñárritu", "media": "movie", "lang": "en",
     "tags": ["survival", "revenge", "dark", "nature", "intense", "grief", "endurance", "brutal", "beautiful", "tense"]},

    {"id": "m034", "title": "Mad Max: Fury Road", "creator": "George Miller", "media": "movie", "lang": "en",
     "tags": ["survival", "freedom", "action", "dark", "feminist", "post-apocalyptic", "intense", "powerful", "rebellion", "high-energy"]},

    {"id": "m035", "title": "The Prestige", "creator": "Christopher Nolan", "media": "movie", "lang": "en",
     "tags": ["obsession", "dark", "clever", "rivalry", "deception", "twist", "tragedy", "sacrifice", "magic", "complex"]},

    {"id": "m036", "title": "Memento", "creator": "Christopher Nolan", "media": "movie", "lang": "en",
     "tags": ["mystery", "dark", "memory", "twist", "identity", "grief", "psychological", "clever", "fragmented", "obsession"]},

    {"id": "m037", "title": "A Beautiful Mind", "creator": "Ron Howard", "media": "movie", "lang": "en",
     "tags": ["genius", "love", "dark", "hope", "mental-health", "bittersweet", "inspiring", "struggle", "beautiful", "redemption"]},

    {"id": "m038", "title": "The Imitation Game", "creator": "Morten Tyldum", "media": "movie", "lang": "en",
     "tags": ["genius", "dark", "war", "identity", "injustice", "bittersweet", "tragic", "sacrifice", "history", "inspiring"]},

    {"id": "m039", "title": "12 Angry Men", "creator": "Sidney Lumet", "media": "movie", "lang": "en",
     "tags": ["justice", "tension", "moral", "society", "dialogue", "intense", "brilliant", "prejudice", "reason", "confined"]},

    {"id": "m040", "title": "To Kill a Mockingbird", "creator": "Robert Mulligan", "media": "movie", "lang": "en",
     "tags": ["justice", "coming-of-age", "racism", "moral", "bittersweet", "nostalgic", "hope", "community", "innocence", "social"]},

    {"id": "m041", "title": "Spirited Away", "creator": "Hayao Miyazaki", "media": "movie", "lang": "en",
     "tags": ["wonder", "magical", "coming-of-age", "adventure", "courage", "whimsical", "dark", "beautiful", "Japanese", "hope"]},

    {"id": "m042", "title": "Up", "creator": "Pete Docter", "media": "movie", "lang": "en",
     "tags": ["love", "grief", "adventure", "bittersweet", "heartwarming", "hope", "wonder", "friendship", "loss", "beautiful"]},

    {"id": "m043", "title": "Inside Out", "creator": "Pete Docter", "media": "movie", "lang": "en",
     "tags": ["emotional", "identity", "bittersweet", "coming-of-age", "joy", "sadness", "beautiful", "psychological", "heartwarming", "wonder"]},

    {"id": "m044", "title": "WALL-E", "creator": "Andrew Stanton", "media": "movie", "lang": "en",
     "tags": ["love", "loneliness", "hope", "environment", "wonder", "bittersweet", "future", "beautiful", "simple", "heartwarming"]},

    {"id": "m045", "title": "Coco", "creator": "Lee Unkrich", "media": "movie", "lang": "en",
     "tags": ["music", "family", "death", "memory", "bittersweet", "love", "Mexican", "beautiful", "heartwarming", "wonder"]},

    {"id": "m046", "title": "The Pianist", "creator": "Roman Polanski", "media": "movie", "lang": "en",
     "tags": ["war", "dark", "music", "survival", "Holocaust", "tragic", "art", "hope", "intense", "human-spirit"]},

    {"id": "m047", "title": "Requiem for a Dream", "creator": "Darren Aronofsky", "media": "movie", "lang": "en",
     "tags": ["dark", "addiction", "despair", "dreams-crushed", "tragic", "intense", "disturbing", "loss", "painful", "raw"]},

    {"id": "m048", "title": "Black Swan", "creator": "Darren Aronofsky", "media": "movie", "lang": "en",
     "tags": ["obsession", "dark", "perfection", "psychological", "ballet", "duality", "intense", "disturbing", "tragic", "complex"]},

    {"id": "m049", "title": "Silver Linings Playbook", "creator": "David O. Russell", "media": "movie", "lang": "en",
     "tags": ["hope", "mental-health", "love", "bittersweet", "healing", "dark-comedy", "resilience", "community", "warm", "uplifting"]},

    {"id": "m050", "title": "American History X", "creator": "Tony Kaye", "media": "movie", "lang": "en",
     "tags": ["dark", "redemption", "race", "transformation", "intense", "family", "hope", "violence", "complex", "tragic"]},

    {"id": "m051", "title": "The Pursuit of Happyness", "creator": "Gabriele Muccino", "media": "movie", "lang": "en",
     "tags": ["hope", "resilience", "fatherhood", "struggle", "inspiring", "dark", "bittersweet", "dreams", "love", "triumph"]},

    {"id": "m052", "title": "Cast Away", "creator": "Robert Zemeckis", "media": "movie", "lang": "en",
     "tags": ["survival", "loneliness", "hope", "isolation", "resilience", "bittersweet", "love", "loss", "nature", "quiet"]},

    {"id": "m053", "title": "Into the Wild", "creator": "Sean Penn", "media": "movie", "lang": "en",
     "tags": ["freedom", "searching", "dark", "nature", "tragic", "youth", "adventure", "philosophy", "bittersweet", "identity"]},

    {"id": "m054", "title": "The Secret Life of Walter Mitty", "creator": "Ben Stiller", "media": "movie", "lang": "en",
     "tags": ["adventure", "wonder", "dreams", "transformation", "hope", "beautiful", "inspiring", "whimsical", "uplifting", "searching"]},

    {"id": "m055", "title": "Pay It Forward", "creator": "Mimi Leder", "media": "movie", "lang": "en",
     "tags": ["hope", "kindness", "dark", "bittersweet", "society", "family", "tragic", "inspiring", "love", "ripple"]},

    {"id": "m056", "title": "Big Fish", "creator": "Tim Burton", "media": "movie", "lang": "en",
     "tags": ["magical", "bittersweet", "father-son", "stories", "wonder", "whimsical", "love", "death", "beautiful", "nostalgic"]},

    {"id": "m057", "title": "About Time", "creator": "Richard Curtis", "media": "movie", "lang": "en",
     "tags": ["love", "family", "bittersweet", "time", "heartwarming", "hope", "beautiful", "wisdom", "grief", "philosophical"]},

    {"id": "m058", "title": "Amélie", "creator": "Jean-Pierre Jeunet", "media": "movie", "lang": "en",
     "tags": ["whimsical", "romantic", "magical", "quirky", "joyful", "bittersweet", "loneliness", "hope", "beautiful", "French"]},

    {"id": "m059", "title": "Pan's Labyrinth", "creator": "Guillermo del Toro", "media": "movie", "lang": "en",
     "tags": ["dark", "magical", "war", "escape", "beautiful", "tragic", "wonder", "dark-fantasy", "bittersweet", "childhood"]},

    {"id": "m060", "title": "The Shape of Water", "creator": "Guillermo del Toro", "media": "movie", "lang": "en",
     "tags": ["love", "dark", "outsider", "magical", "tender", "beautiful", "lonely", "romantic", "whimsical", "bittersweet"]},

    {"id": "m061", "title": "Schindler's List", "creator": "Steven Spielberg", "media": "movie", "lang": "en",
     "tags": ["dark", "hope", "sacrifice", "historical", "war", "humanity", "profound", "redemption", "Holocaust", "tragic"]},

    {"id": "m062", "title": "Dunkirk", "creator": "Christopher Nolan", "media": "movie", "lang": "en",
     "tags": ["war", "survival", "tense", "hope", "dark", "intense", "time", "heroic", "historical", "fragmented"]},

    {"id": "m063", "title": "Atonement", "creator": "Joe Wright", "media": "movie", "lang": "en",
     "tags": ["love", "war", "guilt", "tragic", "beautiful", "bittersweet", "dark", "regret", "loss", "historical"]},

    {"id": "m064", "title": "Pride & Prejudice", "creator": "Joe Wright", "media": "movie", "lang": "en",
     "tags": ["romantic", "bittersweet", "witty", "love", "society", "beautiful", "hope", "class", "independent", "charming"]},

    {"id": "m065", "title": "The English Patient", "creator": "Anthony Minghella", "media": "movie", "lang": "en",
     "tags": ["love", "war", "dark", "bittersweet", "beautiful", "tragic", "memory", "passion", "sacrifice", "lyrical"]},

    {"id": "m066", "title": "Whiplash", "creator": "Damien Chazelle", "media": "movie", "lang": "en",
     "tags": ["obsession", "music", "dark", "intense", "perfection", "driven", "tense", "brilliant", "complex", "ambition"]},

    {"id": "m067", "title": "The Grand Budapest Hotel", "creator": "Wes Anderson", "media": "movie", "lang": "en",
     "tags": ["whimsical", "dark-comedy", "nostalgia", "quirky", "elegant", "friendship", "adventure", "witty", "bittersweet", "charming"]},

    {"id": "m068", "title": "Moonrise Kingdom", "creator": "Wes Anderson", "media": "movie", "lang": "en",
     "tags": ["romantic", "whimsical", "coming-of-age", "love", "adventure", "quirky", "nostalgic", "bittersweet", "tender", "wonder"]},

    {"id": "m069", "title": "The Darjeeling Limited", "creator": "Wes Anderson", "media": "movie", "lang": "en",
     "tags": ["grief", "brotherhood", "India", "bittersweet", "whimsical", "searching", "family", "dark-comedy", "quirky", "healing"]},

    {"id": "m070", "title": "Cloud Atlas", "creator": "Wachowski Sisters", "media": "movie", "lang": "en",
     "tags": ["epic", "love", "philosophical", "dark", "reincarnation", "hope", "complex", "interconnected", "wonder", "sacrifice"]},

    # ── ITALIAN MOVIES (35) ──────────────────────────────────────────────────

    {"id": "mi001", "title": "La Vita è Bella", "creator": "Roberto Benigni", "media": "movie", "lang": "it",
     "tags": ["love", "dark", "hope", "Holocaust", "bittersweet", "family", "humor", "tragic", "father-son", "beautiful"]},

    {"id": "mi002", "title": "Cinema Paradiso", "creator": "Giuseppe Tornatore", "media": "movie", "lang": "it",
     "tags": ["nostalgia", "love", "bittersweet", "cinema", "childhood", "loss", "memory", "beautiful", "melancholic", "friendship"]},

    {"id": "mi003", "title": "The Great Beauty", "creator": "Paolo Sorrentino", "media": "movie", "lang": "it",
     "tags": ["melancholic", "Rome", "beauty", "aging", "dark", "philosophical", "nostalgia", "searching", "decadence", "bittersweet"]},

    {"id": "mi004", "title": "Il Postino", "creator": "Michael Radford", "media": "movie", "lang": "it",
     "tags": ["poetry", "love", "friendship", "bittersweet", "gentle", "beautiful", "simple", "melancholic", "island", "hopeful"]},

    {"id": "mi005", "title": "Roma Città Aperta", "creator": "Roberto Rossellini", "media": "movie", "lang": "it",
     "tags": ["war", "resistance", "dark", "heroic", "sacrifice", "hope", "WWII", "historical", "tragic", "community"]},

    {"id": "mi006", "title": "Ladri di Biciclette", "creator": "Vittorio De Sica", "media": "movie", "lang": "it",
     "tags": ["poverty", "father-son", "tragedy", "Italy", "dark", "social", "bittersweet", "hopeless", "neorealism", "human"]},

    {"id": "mi007", "title": "8½", "creator": "Federico Fellini", "media": "movie", "lang": "it",
     "tags": ["art", "creativity", "surreal", "dark", "identity", "dreamy", "complex", "meta", "introspective", "Italian"]},

    {"id": "mi008", "title": "La Dolce Vita", "creator": "Federico Fellini", "media": "movie", "lang": "it",
     "tags": ["excess", "Rome", "searching", "dark", "nostalgia", "glamour", "melancholic", "decadence", "bittersweet", "iconic"]},

    {"id": "mi009", "title": "Nuovo Cinema Paradiso", "creator": "Giuseppe Tornatore", "media": "movie", "lang": "it",
     "tags": ["cinema", "nostalgia", "love", "bittersweet", "childhood", "memory", "beautiful", "melancholic", "community", "loss"]},

    {"id": "mi010", "title": "The Conformist", "creator": "Bernardo Bertolucci", "media": "movie", "lang": "it",
     "tags": ["fascism", "identity", "dark", "political", "conformity", "psychological", "complex", "beautiful", "guilt", "historical"]},

    {"id": "mi011", "title": "Mediterráneo", "creator": "Gabriele Salvatores", "media": "movie", "lang": "it",
     "tags": ["freedom", "war", "bittersweet", "friendship", "escape", "hope", "humorous", "Mediterranean", "nostalgic", "gentle"]},

    {"id": "mi012", "title": "The Best of Youth", "creator": "Marco Tullio Giordana", "media": "movie", "lang": "it",
     "tags": ["epic", "family", "Italy", "history", "love", "bittersweet", "generational", "hope", "complex", "beautiful"]},

    {"id": "mi013", "title": "L'Avventura", "creator": "Michelangelo Antonioni", "media": "movie", "lang": "it",
     "tags": ["searching", "melancholic", "mystery", "dark", "slow", "emptiness", "modern", "existential", "quiet", "bittersweet"]},

    {"id": "mi014", "title": "Amarcord", "creator": "Federico Fellini", "media": "movie", "lang": "it",
     "tags": ["nostalgia", "Italy", "whimsical", "dark", "bittersweet", "memory", "coming-of-age", "humor", "community", "fascism"]},

    {"id": "mi015", "title": "The Tree of Wooden Clogs", "creator": "Ermanno Olmi", "media": "movie", "lang": "it",
     "tags": ["family", "poverty", "faith", "gentle", "beautiful", "Italy", "pastoral", "bittersweet", "community", "quiet"]},

    {"id": "mi016", "title": "Divorce Italian Style", "creator": "Pietro Germi", "media": "movie", "lang": "it",
     "tags": ["dark-comedy", "satirical", "Italy", "marriage", "humorous", "clever", "bittersweet", "society", "irony", "obsession"]},

    {"id": "mi017", "title": "The Gospel According to St. Matthew", "creator": "Pier Paolo Pasolini", "media": "movie", "lang": "it",
     "tags": ["spiritual", "dark", "faith", "social", "radical", "philosophical", "Italy", "historical", "intense", "powerful"]},

    {"id": "mi018", "title": "Gomorrah", "creator": "Matteo Garrone", "media": "movie", "lang": "it",
     "tags": ["dark", "crime", "Naples", "bleak", "gritty", "tragic", "brutal", "social", "realistic", "intense"]},

    {"id": "mi019", "title": "Youth", "creator": "Paolo Sorrentino", "media": "movie", "lang": "it",
     "tags": ["aging", "dark", "nostalgia", "beauty", "bittersweet", "philosophical", "friendship", "elegant", "art", "searching"]},

    {"id": "mi020", "title": "The Leopard", "creator": "Luchino Visconti", "media": "movie", "lang": "it",
     "tags": ["epic", "Italy", "historical", "aristocracy", "melancholic", "bittersweet", "change", "nostalgia", "elegant", "dark"]},

    {"id": "mi021", "title": "Caos Calmo", "creator": "Antonello Grimaldi", "media": "movie", "lang": "it",
     "tags": ["grief", "love", "dark", "bittersweet", "quiet", "Italy", "introspective", "loss", "searching", "melancholic"]},

    {"id": "mi022", "title": "Come, Come, Come", "creator": "Ferzan Özpetek", "media": "movie", "lang": "it",
     "tags": ["love", "grief", "dark", "bittersweet", "Italy", "loss", "memory", "tender", "emotional", "quiet"]},

    {"id": "mi023", "title": "Perfect Strangers", "creator": "Paolo Genovese", "media": "movie", "lang": "it",
     "tags": ["dark", "comedy", "secrets", "friendship", "marriage", "Italy", "twist", "uncomfortable", "social", "modern"]},

    {"id": "mi024", "title": "The First Beautiful Thing", "creator": "Paolo Virzì", "media": "movie", "lang": "it",
     "tags": ["family", "bittersweet", "Italy", "nostalgia", "dark", "love", "coming-of-age", "memory", "grief", "humor"]},

    {"id": "mi025", "title": "Gomorra (TV)", "creator": "Stefano Sollima", "media": "movie", "lang": "it",
     "tags": ["dark", "crime", "Naples", "power", "gritty", "intense", "violent", "tragic", "realistic", "society"]},

    {"id": "mi026", "title": "Mine Vaganti", "creator": "Ferzan Özpetek", "media": "movie", "lang": "it",
     "tags": ["family", "identity", "Italy", "bittersweet", "humor", "dark", "love", "society", "coming-of-age", "conflict"]},

    {"id": "mi027", "title": "Mid-August Lunch", "creator": "Gianni Di Gregorio", "media": "movie", "lang": "it",
     "tags": ["humorous", "gentle", "Italy", "aging", "family", "heartwarming", "quiet", "simple", "bittersweet", "community"]},

    {"id": "mi028", "title": "The Unknown Woman", "creator": "Giuseppe Tornatore", "media": "movie", "lang": "it",
     "tags": ["dark", "mystery", "tragic", "redemption", "intense", "twist", "sacrifice", "love", "gritty", "haunting"]},

    {"id": "mi029", "title": "Don't Be Afraid", "creator": "Paola Randi", "media": "movie", "lang": "it",
     "tags": ["dark", "hope", "youth", "adventure", "Italy", "searching", "bittersweet", "identity", "quiet", "melancholic"]},

    {"id": "mi030", "title": "The Soloist", "creator": "Joe Wright", "media": "movie", "lang": "it",
     "tags": ["music", "friendship", "hope", "dark", "mental-health", "bittersweet", "social", "redemption", "complex", "human"]},

    {"id": "mi031", "title": "Tomorrow", "creator": "Virzì, Comencini", "media": "movie", "lang": "it",
     "tags": ["hope", "family", "bittersweet", "Italy", "youth", "coming-of-age", "love", "dark", "searching", "hopeful"]},

    {"id": "mi032", "title": "The Hummingbird", "creator": "Sandro Veronesi", "media": "movie", "lang": "it",
     "tags": ["grief", "love", "bittersweet", "Italy", "time", "family", "loss", "dark", "melancholic", "memory"]},

    {"id": "mi033", "title": "Hammamet", "creator": "Gianni Amelio", "media": "movie", "lang": "it",
     "tags": ["dark", "political", "Italy", "aging", "regret", "power", "fall", "melancholic", "bittersweet", "complex"]},

    {"id": "mi034", "title": "Bad Tales", "creator": "Fabio D'Innocenzo", "media": "movie", "lang": "it",
     "tags": ["dark", "Italy", "suburban", "disturbing", "youth", "family", "bleak", "social", "slow", "uncomfortable"]},

    {"id": "mi035", "title": "Ariaferma", "creator": "Leonardo Di Costanzo", "media": "movie", "lang": "it",
     "tags": ["dark", "prison", "Italy", "tension", "quiet", "humanity", "complex", "slow", "bittersweet", "social"]},

    # ── HINDI MOVIES (35) ────────────────────────────────────────────────────

    {"id": "mh001", "title": "Mughal-E-Azam", "creator": "K. Asif", "media": "movie", "lang": "hi",
     "tags": ["epic", "love", "sacrifice", "historical", "dark", "power", "tragic", "passionate", "grand", "Mughal"]},

    {"id": "mh002", "title": "Sholay", "creator": "Ramesh Sippy", "media": "movie", "lang": "hi",
     "tags": ["friendship", "adventure", "dark", "revenge", "iconic", "humor", "heroic", "loss", "classic", "India"]},

    {"id": "mh003", "title": "Dilwale Dulhania Le Jayenge", "creator": "Aditya Chopra", "media": "movie", "lang": "hi",
     "tags": ["romantic", "love", "family", "India", "nostalgic", "hope", "bittersweet", "iconic", "joyful", "charming"]},

    {"id": "mh004", "title": "Lagaan", "creator": "Ashutosh Gowariker", "media": "movie", "lang": "hi",
     "tags": ["resilience", "hope", "dark", "colonial", "community", "sport", "epic", "triumph", "India", "inspirational"]},

    {"id": "mh005", "title": "3 Idiots", "creator": "Rajkumar Hirani", "media": "movie", "lang": "hi",
     "tags": ["friendship", "humor", "hope", "India", "education", "satirical", "heartwarming", "love", "inspirational", "society"]},

    {"id": "mh006", "title": "Dil Chahta Hai", "creator": "Farhan Akhtar", "media": "movie", "lang": "hi",
     "tags": ["friendship", "youth", "coming-of-age", "love", "bittersweet", "modern", "fun", "India", "nostalgic", "heartwarming"]},

    {"id": "mh007", "title": "Taare Zameen Par", "creator": "Aamir Khan", "media": "movie", "lang": "hi",
     "tags": ["childhood", "hope", "dark", "art", "family", "bittersweet", "inspiring", "neurodiversity", "love", "India"]},

    {"id": "mh008", "title": "Rang De Basanti", "creator": "Rakeysh Omprakash Mehra", "media": "movie", "lang": "hi",
     "tags": ["youth", "India", "revolution", "dark", "friendship", "sacrifice", "bittersweet", "passionate", "political", "tragic"]},

    {"id": "mh009", "title": "Black", "creator": "Sanjay Leela Bhansali", "media": "movie", "lang": "hi",
     "tags": ["dark", "resilience", "hope", "disability", "bittersweet", "India", "inspiring", "love", "loss", "beautiful"]},

    {"id": "mh010", "title": "Devdas", "creator": "Sanjay Leela Bhansali", "media": "movie", "lang": "hi",
     "tags": ["tragic", "love", "obsession", "dark", "self-destruction", "bittersweet", "romantic", "India", "melodramatic", "loss"]},

    {"id": "mh011", "title": "Queen", "creator": "Vikas Bahl", "media": "movie", "lang": "hi",
     "tags": ["freedom", "identity", "coming-of-age", "India", "hope", "joyful", "feminist", "adventure", "bittersweet", "uplifting"]},

    {"id": "mh012", "title": "Paan Singh Tomar", "creator": "Tigmanshu Dhulia", "media": "movie", "lang": "hi",
     "tags": ["dark", "India", "resilience", "injustice", "tragic", "sport", "bittersweet", "anger", "social", "true-story"]},

    {"id": "mh013", "title": "Andhadhun", "creator": "Sriram Raghavan", "media": "movie", "lang": "hi",
     "tags": ["dark", "thriller", "clever", "twist", "dark-comedy", "India", "tense", "satirical", "morally-grey", "suspense"]},

    {"id": "mh014", "title": "Dangal", "creator": "Nitesh Tiwari", "media": "movie", "lang": "hi",
     "tags": ["resilience", "hope", "family", "sport", "India", "dark", "bittersweet", "inspiring", "feminist", "triumph"]},

    {"id": "mh015", "title": "Drishyam", "creator": "Nishikant Kamat", "media": "movie", "lang": "hi",
     "tags": ["dark", "family", "thriller", "clever", "India", "tense", "moral", "suspense", "love", "sacrifice"]},

    {"id": "mh016", "title": "Tumbbad", "creator": "Rahi Anil Barve", "media": "movie", "lang": "hi",
     "tags": ["dark", "greed", "horror", "India", "mythological", "atmospheric", "cursed", "bleak", "intense", "unique"]},

    {"id": "mh017", "title": "Article 15", "creator": "Anubhav Sinha", "media": "movie", "lang": "hi",
     "tags": ["dark", "social", "India", "caste", "justice", "anger", "intense", "political", "bittersweet", "realism"]},

    {"id": "mh018", "title": "Gulaal", "creator": "Anurag Kashyap", "media": "movie", "lang": "hi",
     "tags": ["dark", "politics", "India", "tragedy", "intense", "gritty", "power", "bittersweet", "complex", "angry"]},

    {"id": "mh019", "title": "Gangs of Wasseypur", "creator": "Anurag Kashyap", "media": "movie", "lang": "hi",
     "tags": ["dark", "crime", "India", "epic", "gritty", "violent", "family", "revenge", "complex", "tragedy"]},

    {"id": "mh020", "title": "Masaan", "creator": "Neeraj Ghaywan", "media": "movie", "lang": "hi",
     "tags": ["grief", "dark", "India", "bittersweet", "love", "hope", "loss", "quiet", "beautiful", "melancholic"]},

    {"id": "mh021", "title": "Mughal-E-Azam", "creator": "K. Asif", "media": "movie", "lang": "hi",
     "tags": ["epic", "historical", "love", "dark", "power", "sacrifice", "tragic", "grand", "Mughal", "India"]},

    {"id": "mh022", "title": "Kapoor & Sons", "creator": "Shakun Batra", "media": "movie", "lang": "hi",
     "tags": ["family", "dark", "bittersweet", "secrets", "India", "coming-of-age", "grief", "complex", "modern", "love"]},

    {"id": "mh023", "title": "Raazi", "creator": "Meghna Gulzar", "media": "movie", "lang": "hi",
     "tags": ["dark", "sacrifice", "India", "war", "spy", "love", "tragic", "tense", "bittersweet", "intense"]},

    {"id": "mh024", "title": "Zindagi Na Milegi Dobara", "creator": "Zoya Akhtar", "media": "movie", "lang": "hi",
     "tags": ["friendship", "adventure", "hope", "India", "bittersweet", "travel", "coming-of-age", "love", "joyful", "searching"]},

    {"id": "mh025", "title": "Wake Up Sid", "creator": "Ayan Mukerji", "media": "movie", "lang": "hi",
     "tags": ["coming-of-age", "India", "love", "bittersweet", "growth", "friendship", "modern", "hopeful", "charming", "youth"]},

    {"id": "mh026", "title": "Mughal-E-Azam", "creator": "K. Asif", "media": "movie", "lang": "hi",
     "tags": ["epic", "historical", "India", "love", "sacrifice", "power", "grand", "dark", "tragic", "passionate"]},

    {"id": "mh027", "title": "Lunchbox", "creator": "Ritesh Batra", "media": "movie", "lang": "hi",
     "tags": ["loneliness", "connection", "love", "bittersweet", "India", "quiet", "melancholic", "hope", "beautiful", "searching"]},

    {"id": "mh028", "title": "Piku", "creator": "Shoojit Sircar", "media": "movie", "lang": "hi",
     "tags": ["family", "bittersweet", "India", "love", "humor", "aging", "quiet", "beautiful", "gentle", "bittersweet"]},

    {"id": "mh029", "title": "Barfi!", "creator": "Anurag Basu", "media": "movie", "lang": "hi",
     "tags": ["love", "whimsical", "bittersweet", "India", "disability", "heartwarming", "gentle", "beautiful", "nostalgic", "joyful"]},

    {"id": "mh030", "title": "Kaala", "creator": "Pa. Ranjith", "media": "movie", "lang": "hi",
     "tags": ["dark", "India", "social", "power", "resistance", "community", "hope", "political", "intense", "identity"]},

    {"id": "mh031", "title": "Udaan", "creator": "Vikramaditya Motwane", "media": "movie", "lang": "hi",
     "tags": ["coming-of-age", "dark", "India", "freedom", "abuse", "bittersweet", "hope", "youth", "writing", "resilience"]},

    {"id": "mh032", "title": "Dil Dhadakne Do", "creator": "Zoya Akhtar", "media": "movie", "lang": "hi",
     "tags": ["family", "India", "dark", "wealth", "bittersweet", "identity", "love", "humor", "satirical", "complex"]},

    {"id": "mh033", "title": "Newton", "creator": "Amit V. Masurkar", "media": "movie", "lang": "hi",
     "tags": ["dark", "India", "idealism", "democracy", "bittersweet", "quiet", "satirical", "hope", "integrity", "simple"]},

    {"id": "mh034", "title": "Ship of Theseus", "creator": "Anand Gandhi", "media": "movie", "lang": "hi",
     "tags": ["philosophical", "India", "identity", "beautiful", "bittersweet", "wonder", "quiet", "introspective", "dark", "art"]},

    {"id": "mh035", "title": "Lootera", "creator": "Vikramaditya Motwane", "media": "movie", "lang": "hi",
     "tags": ["love", "dark", "bittersweet", "India", "historical", "melancholic", "beautiful", "loss", "longing", "quiet"]},

    # ── ENGLISH SONGS (55) ───────────────────────────────────────────────────

    {"id": "s001", "title": "Bohemian Rhapsody", "creator": "Queen", "media": "song", "lang": "en",
     "tags": ["epic", "dark", "identity", "theatrical", "iconic", "emotional", "complex", "rebellious", "dramatic", "powerful"]},

    {"id": "s002", "title": "Hallelujah", "creator": "Leonard Cohen", "media": "song", "lang": "en",
     "tags": ["melancholic", "spiritual", "bittersweet", "love-lost", "beautiful", "grief", "longing", "profound", "serene", "poetry"]},

    {"id": "s003", "title": "Yesterday", "creator": "The Beatles", "media": "song", "lang": "en",
     "tags": ["nostalgia", "melancholic", "love-lost", "bittersweet", "longing", "grief", "beautiful", "simple", "iconic", "yearning"]},

    {"id": "s004", "title": "Hotel California", "creator": "Eagles", "media": "song", "lang": "en",
     "tags": ["dark", "mysterious", "trapped", "excess", "haunting", "iconic", "American", "disillusion", "addictive", "surreal"]},

    {"id": "s005", "title": "Stairway to Heaven", "creator": "Led Zeppelin", "media": "song", "lang": "en",
     "tags": ["epic", "spiritual", "journey", "mystical", "wonder", "dark", "iconic", "transcendent", "emotional", "deep"]},

    {"id": "s006", "title": "Imagine", "creator": "John Lennon", "media": "song", "lang": "en",
     "tags": ["hope", "peace", "philosophical", "idealistic", "beautiful", "serene", "inspirational", "utopian", "iconic", "gentle"]},

    {"id": "s007", "title": "Sound of Silence", "creator": "Simon & Garfunkel", "media": "song", "lang": "en",
     "tags": ["loneliness", "dark", "alienation", "poetic", "melancholic", "introspective", "iconic", "modern", "haunting", "profound"]},

    {"id": "s008", "title": "Hurt", "creator": "Nine Inch Nails", "media": "song", "lang": "en",
     "tags": ["dark", "pain", "addiction", "self-destruction", "grief", "haunting", "raw", "melancholic", "intense", "regret"]},

    {"id": "s009", "title": "Comfortably Numb", "creator": "Pink Floyd", "media": "song", "lang": "en",
     "tags": ["dark", "disconnection", "melancholic", "dreamy", "introspective", "haunting", "grief", "numbness", "beautiful", "epic"]},

    {"id": "s010", "title": "The Sound of Silence", "creator": "Simon & Garfunkel", "media": "song", "lang": "en",
     "tags": ["loneliness", "alienation", "dark", "philosophical", "melancholic", "haunting", "poetic", "society", "introspective", "iconic"]},

    {"id": "s011", "title": "Wish You Were Here", "creator": "Pink Floyd", "media": "song", "lang": "en",
     "tags": ["longing", "friendship", "loss", "melancholic", "dark", "bittersweet", "introspective", "beautiful", "yearning", "grief"]},

    {"id": "s012", "title": "Smells Like Teen Spirit", "creator": "Nirvana", "media": "song", "lang": "en",
     "tags": ["rebellious", "dark", "youth", "anger", "disillusion", "iconic", "energetic", "frustration", "generation", "raw"]},

    {"id": "s013", "title": "Creep", "creator": "Radiohead", "media": "song", "lang": "en",
     "tags": ["loneliness", "self-loathing", "dark", "yearning", "identity", "melancholic", "raw", "outsider", "longing", "emotional"]},

    {"id": "s014", "title": "Fake Plastic Trees", "creator": "Radiohead", "media": "song", "lang": "en",
     "tags": ["dark", "emptiness", "modern", "melancholic", "society", "hollow", "bittersweet", "longing", "introspective", "beautiful"]},

    {"id": "s015", "title": "Fast Car", "creator": "Tracy Chapman", "media": "song", "lang": "en",
     "tags": ["hope", "escape", "poverty", "love", "bittersweet", "longing", "freedom", "dark", "nostalgia", "working-class"]},

    {"id": "s016", "title": "What's Going On", "creator": "Marvin Gaye", "media": "song", "lang": "en",
     "tags": ["social", "hope", "dark", "war", "love", "political", "beautiful", "peaceful", "soul", "profound"]},

    {"id": "s017", "title": "Redemption Song", "creator": "Bob Marley", "media": "song", "lang": "en",
     "tags": ["freedom", "hope", "spiritual", "dark", "resilience", "peaceful", "beautiful", "political", "inspiring", "historical"]},

    {"id": "s018", "title": "Space Oddity", "creator": "David Bowie", "media": "song", "lang": "en",
     "tags": ["lonely", "dark", "space", "surreal", "bittersweet", "iconic", "melancholic", "detached", "beautiful", "searching"]},

    {"id": "s019", "title": "Heroes", "creator": "David Bowie", "media": "song", "lang": "en",
     "tags": ["hope", "love", "triumph", "dark", "bittersweet", "iconic", "powerful", "beautiful", "inspiring", "fleeting"]},

    {"id": "s020", "title": "Running Up That Hill", "creator": "Kate Bush", "media": "song", "lang": "en",
     "tags": ["longing", "dark", "bittersweet", "love", "empathy", "haunting", "passionate", "ethereal", "hopeful", "intense"]},

    {"id": "s021", "title": "Fix You", "creator": "Coldplay", "media": "song", "lang": "en",
     "tags": ["hope", "love", "healing", "bittersweet", "beautiful", "loss", "comfort", "emotional", "gentle", "uplifting"]},

    {"id": "s022", "title": "The Scientist", "creator": "Coldplay", "media": "song", "lang": "en",
     "tags": ["regret", "love-lost", "melancholic", "bittersweet", "longing", "beautiful", "introspective", "yearning", "dark", "gentle"]},

    {"id": "s023", "title": "Skinny Love", "creator": "Bon Iver", "media": "song", "lang": "en",
     "tags": ["dark", "love-lost", "raw", "grief", "melancholic", "bittersweet", "longing", "introspective", "painful", "beautiful"]},

    {"id": "s024", "title": "Holocene", "creator": "Bon Iver", "media": "song", "lang": "en",
     "tags": ["melancholic", "beautiful", "introspective", "nature", "bittersweet", "ethereal", "longing", "serene", "nostalgic", "quiet"]},

    {"id": "s025", "title": "Black", "creator": "Pearl Jam", "media": "song", "lang": "en",
     "tags": ["love-lost", "grief", "dark", "yearning", "raw", "melancholic", "passionate", "intense", "bittersweet", "painful"]},

    {"id": "s026", "title": "Bittersweet Symphony", "creator": "The Verve", "media": "song", "lang": "en",
     "tags": ["bittersweet", "life", "freedom", "longing", "melancholic", "iconic", "cinematic", "searching", "deep", "trapped"]},

    {"id": "s027", "title": "Mad World", "creator": "Gary Jules", "media": "song", "lang": "en",
     "tags": ["dark", "melancholic", "lonely", "society", "despair", "hauting", "introspective", "quiet", "bittersweet", "bleak"]},

    {"id": "s028", "title": "The Night We Met", "creator": "Lord Huron", "media": "song", "lang": "en",
     "tags": ["nostalgia", "dark", "longing", "love-lost", "bittersweet", "haunting", "melancholic", "yearning", "beautiful", "grief"]},

    {"id": "s029", "title": "Someone Like You", "creator": "Adele", "media": "song", "lang": "en",
     "tags": ["love-lost", "bittersweet", "grief", "longing", "melancholic", "beautiful", "powerful", "raw", "emotional", "acceptance"]},

    {"id": "s030", "title": "Rolling in the Deep", "creator": "Adele", "media": "song", "lang": "en",
     "tags": ["anger", "betrayal", "powerful", "passionate", "revenge", "grief", "dark", "energetic", "raw", "cathartic"]},

    {"id": "s031", "title": "All I Want", "creator": "Kodaline", "media": "song", "lang": "en",
     "tags": ["love-lost", "grief", "longing", "dark", "bittersweet", "beautiful", "raw", "yearning", "melancholic", "painful"]},

    {"id": "s032", "title": "Slow Dancing in a Burning Room", "creator": "John Mayer", "media": "song", "lang": "en",
     "tags": ["love-lost", "dark", "melancholic", "bittersweet", "passionate", "painful", "beautiful", "longing", "intimate", "raw"]},

    {"id": "s033", "title": "Gravity", "creator": "John Mayer", "media": "song", "lang": "en",
     "tags": ["struggle", "dark", "introspective", "beautiful", "melancholic", "identity", "bittersweet", "honest", "searching", "weight"]},

    {"id": "s034", "title": "Vienna", "creator": "Billy Joel", "media": "song", "lang": "en",
     "tags": ["wisdom", "slow-down", "bittersweet", "youth", "beautiful", "introspective", "hopeful", "philosophical", "gentle", "searching"]},

    {"id": "s035", "title": "Piano Man", "creator": "Billy Joel", "media": "song", "lang": "en",
     "tags": ["nostalgia", "community", "loneliness", "bittersweet", "beautiful", "story", "bar", "dreams-deferred", "melancholic", "warmth"]},

    {"id": "s036", "title": "Landslide", "creator": "Fleetwood Mac", "media": "song", "lang": "en",
     "tags": ["nostalgia", "change", "bittersweet", "aging", "love", "melancholic", "introspective", "beautiful", "acceptance", "quiet"]},

    {"id": "s037", "title": "The Chain", "creator": "Fleetwood Mac", "media": "song", "lang": "en",
     "tags": ["dark", "love", "anger", "betrayal", "bittersweet", "powerful", "iconic", "energetic", "complex", "tense"]},

    {"id": "s038", "title": "Dancing in the Dark", "creator": "Bruce Springsteen", "media": "song", "lang": "en",
     "tags": ["loneliness", "restless", "dark", "longing", "hope", "searching", "bittersweet", "working-class", "energetic", "America"]},

    {"id": "s039", "title": "Born to Run", "creator": "Bruce Springsteen", "media": "song", "lang": "en",
     "tags": ["freedom", "youth", "hope", "America", "rebellious", "energetic", "longing", "passionate", "escape", "iconic"]},

    {"id": "s040", "title": "Champagne Supernova", "creator": "Oasis", "media": "song", "lang": "en",
     "tags": ["nostalgia", "dreamy", "bittersweet", "youth", "searching", "beautiful", "melancholic", "hazy", "iconic", "hopeful"]},

    {"id": "s041", "title": "Let It Be", "creator": "The Beatles", "media": "song", "lang": "en",
     "tags": ["hope", "acceptance", "peaceful", "spiritual", "bittersweet", "beautiful", "serene", "comfort", "wisdom", "gentle"]},

    {"id": "s042", "title": "Golden", "creator": "Harry Styles", "media": "song", "lang": "en",
     "tags": ["joyful", "longing", "love", "beautiful", "hopeful", "energetic", "bittersweet", "summer", "youthful", "radiant"]},

    {"id": "s043", "title": "Exile", "creator": "Taylor Swift ft. Bon Iver", "media": "song", "lang": "en",
     "tags": ["love-lost", "dark", "grief", "misunderstanding", "bittersweet", "duet", "painful", "beautiful", "yearning", "raw"]},

    {"id": "s044", "title": "All Too Well", "creator": "Taylor Swift", "media": "song", "lang": "en",
     "tags": ["nostalgia", "love-lost", "grief", "dark", "bittersweet", "powerful", "yearning", "detailed", "angry", "raw"]},

    {"id": "s045", "title": "Motion Sickness", "creator": "Phoebe Bridgers", "media": "song", "lang": "en",
     "tags": ["bittersweet", "love-lost", "dark", "introspective", "melancholic", "raw", "funny", "grief", "anger", "indie"]},

    {"id": "s046", "title": "Funeral", "creator": "Phoebe Bridgers", "media": "song", "lang": "en",
     "tags": ["dark", "grief", "beautiful", "introspective", "melancholic", "haunting", "death", "bittersweet", "quiet", "ethereal"]},

    {"id": "s047", "title": "Moon Song", "creator": "Phoebe Bridgers", "media": "song", "lang": "en",
     "tags": ["love", "dark", "bittersweet", "beautiful", "longing", "quiet", "melancholic", "yearning", "tender", "introspective"]},

    {"id": "s048", "title": "Liability", "creator": "Lorde", "media": "song", "lang": "en",
     "tags": ["loneliness", "dark", "bittersweet", "self-acceptance", "raw", "melancholic", "identity", "introspective", "honest", "painful"]},

    {"id": "s049", "title": "Green Light", "creator": "Lorde", "media": "song", "lang": "en",
     "tags": ["hope", "bittersweet", "love-lost", "energetic", "cathartic", "freedom", "yearning", "beautiful", "dancing", "transition"]},

    {"id": "s050", "title": "Ribs", "creator": "Lorde", "media": "song", "lang": "en",
     "tags": ["fear", "growing-up", "dark", "anxiety", "bittersweet", "youth", "intense", "raw", "coming-of-age", "introspective"]},

    {"id": "s051", "title": "Mr. Brightside", "creator": "The Killers", "media": "song", "lang": "en",
     "tags": ["jealousy", "obsession", "dark", "love-lost", "energetic", "bittersweet", "iconic", "raw", "anxiety", "passionate"]},

    {"id": "s052", "title": "The Night Will Always Win", "creator": "James", "media": "song", "lang": "en",
     "tags": ["dark", "hope", "bittersweet", "melancholic", "beautiful", "longing", "haunting", "seeking", "grief", "quiet"]},

    {"id": "s053", "title": "Clocks", "creator": "Coldplay", "media": "song", "lang": "en",
     "tags": ["urgency", "bittersweet", "dark", "time", "searching", "energetic", "melancholic", "beautiful", "tense", "yearning"]},

    {"id": "s054", "title": "Yellow", "creator": "Coldplay", "media": "song", "lang": "en",
     "tags": ["love", "devotion", "beautiful", "hopeful", "gentle", "bittersweet", "pure", "radiant", "tender", "joyful"]},

    {"id": "s055", "title": "The Bones", "creator": "Maren Morris", "media": "song", "lang": "en",
     "tags": ["love", "resilience", "hopeful", "beautiful", "bittersweet", "commitment", "gentle", "country", "trust", "foundation"]},

    # ── ITALIAN SONGS (35) ───────────────────────────────────────────────────

    {"id": "si001", "title": "Azzurro", "creator": "Adriano Celentano", "media": "song", "lang": "it",
     "tags": ["longing", "summer", "bittersweet", "love", "nostalgia", "joyful", "light", "beautiful", "Italy", "yearning"]},

    {"id": "si002", "title": "Nel Blu Dipinto di Blu", "creator": "Domenico Modugno", "media": "song", "lang": "it",
     "tags": ["freedom", "joy", "dreamy", "beautiful", "hope", "soaring", "love", "Italy", "iconic", "light"]},

    {"id": "si003", "title": "Con Te Partirò", "creator": "Andrea Bocelli", "media": "song", "lang": "it",
     "tags": ["love", "longing", "bittersweet", "beautiful", "powerful", "farewell", "epic", "passionate", "hopeful", "Italy"]},

    {"id": "si004", "title": "Bella Ciao", "creator": "Traditional", "media": "song", "lang": "it",
     "tags": ["freedom", "resistance", "dark", "sacrifice", "hope", "Italy", "political", "bittersweet", "historical", "powerful"]},

    {"id": "si005", "title": "Grande Grande Grande", "creator": "Mina", "media": "song", "lang": "it",
     "tags": ["passionate", "love", "joyful", "powerful", "romantic", "energetic", "Italy", "beautiful", "feminine", "iconic"]},

    {"id": "si006", "title": "Almeno Tu nell'Universo", "creator": "Mia Martini", "media": "song", "lang": "it",
     "tags": ["love", "loneliness", "beautiful", "melancholic", "longing", "bittersweet", "powerful", "dark", "Italy", "profound"]},

    {"id": "si007", "title": "Un'Estate Italiana", "creator": "Gianna Nannini & Edoardo Bennato", "media": "song", "lang": "it",
     "tags": ["summer", "joyful", "nostalgia", "Italy", "community", "hopeful", "energetic", "bittersweet", "iconic", "light"]},

    {"id": "si008", "title": "L'Italiano", "creator": "Toto Cutugno", "media": "song", "lang": "it",
     "tags": ["identity", "nostalgia", "Italy", "pride", "longing", "beautiful", "bittersweet", "simple", "iconic", "warmth"]},

    {"id": "si009", "title": "Io Che Non Vivo", "creator": "Pino Donaggio", "media": "song", "lang": "it",
     "tags": ["love", "longing", "bittersweet", "melancholic", "dark", "beautiful", "Italy", "powerful", "yearning", "loss"]},

    {"id": "si010", "title": "Caruso", "creator": "Lucio Dalla", "media": "song", "lang": "it",
     "tags": ["love", "death", "bittersweet", "beautiful", "melancholic", "Italy", "opera", "nostalgia", "profound", "loss"]},

    {"id": "si011", "title": "La Canzone di Marinella", "creator": "Fabrizio De André", "media": "song", "lang": "it",
     "tags": ["tragic", "dark", "poetry", "bittersweet", "Italy", "story", "death", "beautiful", "melancholic", "social"]},

    {"id": "si012", "title": "Via del Campo", "creator": "Fabrizio De André", "media": "song", "lang": "it",
     "tags": ["dark", "social", "Italy", "poverty", "bittersweet", "poetry", "beautiful", "tragic", "compassion", "street"]},

    {"id": "si013", "title": "Il Pescatore", "creator": "Fabrizio De André", "media": "song", "lang": "it",
     "tags": ["peaceful", "story", "gentle", "Italy", "wisdom", "dark", "sea", "bittersweet", "beautiful", "simple"]},

    {"id": "si014", "title": "Bocca di Rosa", "creator": "Fabrizio De André", "media": "song", "lang": "it",
     "tags": ["story", "dark-comedy", "Italy", "society", "bittersweet", "love", "social", "witty", "feminine", "beautiful"]},

    {"id": "si015", "title": "P.C.C.", "creator": "Fabrizio De André", "media": "song", "lang": "it",
     "tags": ["dark", "social", "Italy", "political", "satirical", "bittersweet", "powerful", "complex", "poetic", "protest"]},

    {"id": "si016", "title": "Battisti – Il Tempo di Morire", "creator": "Lucio Battisti", "media": "song", "lang": "it",
     "tags": ["dark", "love", "melancholic", "Italy", "bittersweet", "longing", "poetic", "loss", "beautiful", "romantic"]},

    {"id": "si017", "title": "Ancora", "creator": "Eduardo De Crescenzo", "media": "song", "lang": "it",
     "tags": ["love", "longing", "beautiful", "bittersweet", "melancholic", "Italy", "romantic", "yearning", "gentle", "loss"]},

    {"id": "si018", "title": "Vorrei Che Fosse Amore", "creator": "Mina", "media": "song", "lang": "it",
     "tags": ["love", "bittersweet", "melancholic", "beautiful", "Italy", "longing", "romantic", "dark", "yearning", "passionate"]},

    {"id": "si019", "title": "La Prima Cosa Bella", "creator": "Nicola Di Bari", "media": "song", "lang": "it",
     "tags": ["nostalgia", "love", "bittersweet", "beautiful", "Italy", "gentle", "memory", "melancholic", "longing", "simple"]},

    {"id": "si020", "title": "Perdere l'Amore", "creator": "Massimo Ranieri", "media": "song", "lang": "it",
     "tags": ["love-lost", "melancholic", "bittersweet", "beautiful", "Italy", "dark", "longing", "grief", "powerful", "loss"]},

    {"id": "si021", "title": "Insieme: 1992", "creator": "Toto Cutugno", "media": "song", "lang": "it",
     "tags": ["hope", "Europe", "unity", "Italy", "joyful", "inspirational", "community", "bittersweet", "nostalgic", "political"]},

    {"id": "si022", "title": "A modo mio", "creator": "Adriano Celentano", "media": "song", "lang": "it",
     "tags": ["love", "identity", "bittersweet", "Italy", "beautiful", "passionate", "nostalgic", "romantic", "independent", "dark"]},

    {"id": "si023", "title": "Che Sarà", "creator": "José Feliciano", "media": "song", "lang": "it",
     "tags": ["hope", "longing", "bittersweet", "Italy", "future", "philosophical", "beautiful", "gentle", "melancholic", "searching"]},

    {"id": "si024", "title": "Rolls Royce", "creator": "Achille Lauro", "media": "song", "lang": "it",
     "tags": ["rebellious", "dark", "modern", "Italy", "identity", "provocative", "complex", "unique", "avant-garde", "edgy"]},

    {"id": "si025", "title": "Soldi", "creator": "Mahmood", "media": "song", "lang": "it",
     "tags": ["identity", "family", "bittersweet", "Italy", "dark", "cultural", "modern", "loss", "beautiful", "complex"]},

    {"id": "si026", "title": "Occidentali's Karma", "creator": "Francesco Gabbani", "media": "song", "lang": "it",
     "tags": ["satirical", "philosophical", "modern", "Italy", "humorous", "society", "quirky", "bittersweet", "clever", "provocative"]},

    {"id": "si027", "title": "Ciao Ciao", "creator": "La Rappresentante di Lista", "media": "song", "lang": "it",
     "tags": ["dark", "modern", "Italy", "energetic", "rebellious", "bittersweet", "quirky", "unique", "art", "provocative"]},

    {"id": "si028", "title": "Zitti e Buoni", "creator": "Måneskin", "media": "song", "lang": "it",
     "tags": ["rebellious", "dark", "Italy", "energetic", "youth", "anger", "powerful", "rock", "modern", "freedom"]},

    {"id": "si029", "title": "I Wanna Be Your Slave", "creator": "Måneskin", "media": "song", "lang": "it",
     "tags": ["dark", "rebellious", "passionate", "Italy", "rock", "edgy", "obsession", "modern", "energetic", "provocative"]},

    {"id": "si030", "title": "Tutta Colpa Mia", "creator": "Elisa", "media": "song", "lang": "it",
     "tags": ["love-lost", "bittersweet", "Italy", "melancholic", "beautiful", "grief", "dark", "yearning", "raw", "honest"]},

    {"id": "si031", "title": "Luce (Tramonti a Nord Est)", "creator": "Elisa", "media": "song", "lang": "it",
     "tags": ["beautiful", "bittersweet", "Italy", "love", "nostalgia", "melancholic", "gentle", "emotional", "longing", "ethereal"]},

    {"id": "si032", "title": "Meraviglioso", "creator": "Domenico Modugno", "media": "song", "lang": "it",
     "tags": ["hope", "joy", "Italy", "beautiful", "life", "gentle", "inspirational", "bittersweet", "philosophical", "light"]},

    {"id": "si033", "title": "Penelope", "creator": "Fabrizio De André", "media": "song", "lang": "it",
     "tags": ["love", "longing", "Italy", "bittersweet", "mythological", "beautiful", "waiting", "melancholic", "yearning", "poetic"]},

    {"id": "si034", "title": "Quello che le donne non dicono", "creator": "Fiorella Mannoia", "media": "song", "lang": "it",
     "tags": ["feminist", "bittersweet", "Italy", "society", "honest", "dark", "wit", "women", "complex", "satirical"]},

    {"id": "si035", "title": "Vivo per lei", "creator": "Andrea Bocelli", "media": "song", "lang": "it",
     "tags": ["love", "music", "beautiful", "Italy", "passionate", "powerful", "hopeful", "bittersweet", "art", "devotion"]},

    # ── HINDI SONGS (40) ─────────────────────────────────────────────────────

    {"id": "sh001", "title": "Tum Hi Ho", "creator": "Arijit Singh", "media": "song", "lang": "hi",
     "tags": ["love", "longing", "bittersweet", "beautiful", "melancholic", "devotion", "India", "romantic", "yearning", "dark"]},

    {"id": "sh002", "title": "Kal Ho Naa Ho", "creator": "Sonu Nigam", "media": "song", "lang": "hi",
     "tags": ["hope", "life", "bittersweet", "beautiful", "death", "love", "India", "gentle", "philosophical", "inspiring"]},

    {"id": "sh003", "title": "Phir Le Aya Dil", "creator": "Rekha Bhardwaj", "media": "song", "lang": "hi",
     "tags": ["love-lost", "melancholic", "bittersweet", "India", "dark", "haunting", "beautiful", "longing", "grief", "raw"]},

    {"id": "sh004", "title": "Ae Dil Hai Mushkil", "creator": "Arijit Singh", "media": "song", "lang": "hi",
     "tags": ["love-lost", "dark", "bittersweet", "India", "yearning", "grief", "raw", "melancholic", "beautiful", "painful"]},

    {"id": "sh005", "title": "Lag Ja Gale", "creator": "Lata Mangeshkar", "media": "song", "lang": "hi",
     "tags": ["love", "longing", "bittersweet", "beautiful", "India", "melancholic", "nostalgic", "tender", "iconic", "gentle"]},

    {"id": "sh006", "title": "Channa Mereya", "creator": "Arijit Singh", "media": "song", "lang": "hi",
     "tags": ["love-lost", "grief", "bittersweet", "India", "dark", "beautiful", "melancholic", "yearning", "raw", "passionate"]},

    {"id": "sh007", "title": "Kabhi Kabhi Mere Dil Mein", "creator": "Mukesh", "media": "song", "lang": "hi",
     "tags": ["love", "philosophical", "beautiful", "India", "nostalgic", "romantic", "bittersweet", "poetic", "gentle", "longing"]},

    {"id": "sh008", "title": "Dil Se Re", "creator": "A.R. Rahman", "media": "song", "lang": "hi",
     "tags": ["passionate", "dark", "obsession", "India", "powerful", "yearning", "bittersweet", "intense", "love", "beautiful"]},

    {"id": "sh009", "title": "Tujhse Naraaz Nahi", "creator": "Lata Mangeshkar", "media": "song", "lang": "hi",
     "tags": ["bittersweet", "love", "gentle", "India", "melancholic", "beautiful", "forgiveness", "tender", "loss", "nostalgic"]},

    {"id": "sh010", "title": "Ek Pyaar Ka Nagma Hai", "creator": "Lata Mangeshkar", "media": "song", "lang": "hi",
     "tags": ["love", "peaceful", "gentle", "beautiful", "India", "hopeful", "nostalgic", "serene", "simple", "devotion"]},

    {"id": "sh011", "title": "Tere Bina", "creator": "Gulzar", "media": "song", "lang": "hi",
     "tags": ["loneliness", "love", "melancholic", "bittersweet", "India", "dark", "longing", "beautiful", "poetic", "introspective"]},

    {"id": "sh012", "title": "Aaj Jaane Ki Zid Na Karo", "creator": "Farida Khanum", "media": "song", "lang": "hi",
     "tags": ["love", "bittersweet", "longing", "India", "beautiful", "dark", "romantic", "longing", "classic", "tender"]},

    {"id": "sh013", "title": "O Re Piya", "creator": "Rahat Fateh Ali Khan", "media": "song", "lang": "hi",
     "tags": ["love", "longing", "beautiful", "India", "bittersweet", "romantic", "melancholic", "yearning", "peaceful", "spiritual"]},

    {"id": "sh014", "title": "Dil Dhadakne Do", "creator": "Priyanka Chopra & Farhan Akhtar", "media": "song", "lang": "hi",
     "tags": ["hope", "freedom", "India", "joyful", "bittersweet", "searching", "adventure", "beautiful", "uplifting", "dreamy"]},

    {"id": "sh015", "title": "Alvida", "creator": "K.K.", "media": "song", "lang": "hi",
     "tags": ["farewell", "love-lost", "dark", "bittersweet", "India", "melancholic", "grief", "beautiful", "yearning", "loss"]},

    {"id": "sh016", "title": "Zinda", "creator": "Siddharth Mahadevan", "media": "song", "lang": "hi",
     "tags": ["hope", "resilience", "India", "inspirational", "dark", "beautiful", "energetic", "powerful", "uplifting", "struggle"]},

    {"id": "sh017", "title": "Ik Onkar", "creator": "A.R. Rahman", "media": "song", "lang": "hi",
     "tags": ["spiritual", "beautiful", "India", "faith", "peaceful", "profound", "serene", "devotion", "hope", "powerful"]},

    {"id": "sh018", "title": "Maa", "creator": "Taare Zameen Par", "media": "song", "lang": "hi",
     "tags": ["love", "grief", "dark", "bittersweet", "India", "beautiful", "motherhood", "longing", "tender", "emotional"]},

    {"id": "sh019", "title": "Khaabon Ke Parindey", "creator": "Mohit Chauhan", "media": "song", "lang": "hi",
     "tags": ["freedom", "dreams", "India", "hopeful", "bittersweet", "beautiful", "searching", "youth", "adventure", "gentle"]},

    {"id": "sh020", "title": "Kun Faya Kun", "creator": "A.R. Rahman", "media": "song", "lang": "hi",
     "tags": ["spiritual", "beautiful", "India", "peaceful", "transcendent", "devotion", "serene", "faith", "hope", "profound"]},

    {"id": "sh021", "title": "Tujhe Bhula Diya", "creator": "Mohit Chauhan & Shekhar Ravjiani", "media": "song", "lang": "hi",
     "tags": ["love-lost", "dark", "bittersweet", "India", "melancholic", "grief", "beautiful", "yearning", "painful", "haunting"]},

    {"id": "sh022", "title": "Ilahi", "creator": "Arijit Singh", "media": "song", "lang": "hi",
     "tags": ["spiritual", "hopeful", "India", "beautiful", "serene", "faith", "bittersweet", "gentle", "peaceful", "devotion"]},

    {"id": "sh023", "title": "Jo Bhi Main", "creator": "Mohit Chauhan", "media": "song", "lang": "hi",
     "tags": ["identity", "introspective", "India", "beautiful", "bittersweet", "searching", "gentle", "hopeful", "philosophical", "melancholic"]},

    {"id": "sh024", "title": "Agar Tum Saath Ho", "creator": "Arijit Singh & Alka Yagnik", "media": "song", "lang": "hi",
     "tags": ["love-lost", "dark", "bittersweet", "India", "grief", "painful", "raw", "beautiful", "melancholic", "loss"]},

    {"id": "sh025", "title": "Naina", "creator": "Arnav Bose", "media": "song", "lang": "hi",
     "tags": ["love", "longing", "India", "dark", "melancholic", "bittersweet", "beautiful", "yearning", "gentle", "romantic"]},

    {"id": "sh026", "title": "Bulleya", "creator": "Amit Mishra", "media": "song", "lang": "hi",
     "tags": ["spiritual", "India", "Sufi", "beautiful", "philosophical", "bittersweet", "searching", "devotion", "love", "transcendent"]},

    {"id": "sh027", "title": "Mere Dholna", "creator": "Shreya Ghoshal", "media": "song", "lang": "hi",
     "tags": ["love", "devotion", "India", "beautiful", "passionate", "bittersweet", "folk", "gentle", "cultural", "longing"]},

    {"id": "sh028", "title": "Tere Liye", "creator": "Atif Aslam", "media": "song", "lang": "hi",
     "tags": ["love", "sacrifice", "India", "bittersweet", "beautiful", "dark", "devotion", "melancholic", "romantic", "yearning"]},

    {"id": "sh029", "title": "Ehsaas", "creator": "Udit Narayan", "media": "song", "lang": "hi",
     "tags": ["love", "bittersweet", "India", "gentle", "melancholic", "beautiful", "nostalgic", "romantic", "tender", "longing"]},

    {"id": "sh030", "title": "Dil Diyan Gallan", "creator": "Atif Aslam", "media": "song", "lang": "hi",
     "tags": ["love", "romantic", "India", "beautiful", "hopeful", "gentle", "bittersweet", "warmth", "devotion", "longing"]},

    {"id": "sh031", "title": "Kabira", "creator": "Rekha Bhardwaj & Tochi Raina", "media": "song", "lang": "hi",
     "tags": ["love-lost", "bittersweet", "dark", "India", "melancholic", "grief", "beautiful", "yearning", "poetic", "spiritual"]},

    {"id": "sh032", "title": "Raabta", "creator": "Arijit Singh", "media": "song", "lang": "hi",
     "tags": ["love", "spiritual", "India", "beautiful", "bittersweet", "longing", "hopeful", "gentle", "devotion", "connection"]},

    {"id": "sh033", "title": "Jashn-E-Bahara", "creator": "Javed Ali", "media": "song", "lang": "hi",
     "tags": ["beautiful", "love", "India", "nature", "romantic", "peaceful", "gentle", "hopeful", "bittersweet", "poetic"]},

    {"id": "sh034", "title": "Teri Mitti", "creator": "B. Praak", "media": "song", "lang": "hi",
     "tags": ["sacrifice", "dark", "India", "war", "bittersweet", "patriotic", "grief", "loss", "beautiful", "emotional"]},

    {"id": "sh035", "title": "Toota Jo Kabhi Tara", "creator": "Atif Aslam", "media": "song", "lang": "hi",
     "tags": ["love", "bittersweet", "India", "melancholic", "beautiful", "dark", "yearning", "grief", "romantic", "gentle"]},

    {"id": "sh036", "title": "Sawan Aaya Hai", "creator": "Arijit Singh", "media": "song", "lang": "hi",
     "tags": ["dark", "grief", "love-lost", "India", "bittersweet", "melancholic", "beautiful", "raw", "yearning", "painful"]},

    {"id": "sh037", "title": "Khali Khali Dil Ko", "creator": "Mohd. Irfan", "media": "song", "lang": "hi",
     "tags": ["loneliness", "dark", "India", "melancholic", "bittersweet", "grief", "beautiful", "yearning", "loss", "searching"]},

    {"id": "sh038", "title": "Qaafi", "creator": "Shafqat Amanat Ali", "media": "song", "lang": "hi",
     "tags": ["spiritual", "India", "Sufi", "beautiful", "philosophical", "devotion", "transcendent", "searching", "serene", "bittersweet"]},

    {"id": "sh039", "title": "Woh Lamhe", "creator": "Atif Aslam", "media": "song", "lang": "hi",
     "tags": ["nostalgia", "love-lost", "bittersweet", "India", "melancholic", "dark", "beautiful", "yearning", "grief", "memory"]},

    {"id": "sh040", "title": "Dum Maaro Dum", "creator": "Asha Bhosle", "media": "song", "lang": "hi",
     "tags": ["rebellious", "dark", "India", "freedom", "psychedelic", "bittersweet", "cultural", "iconic", "edgy", "searching"]},
]

# ── Tag taxonomy for reference ──────────────────────────────────────────────
ALL_TAGS = sorted(set(tag for item in CATALOG for tag in item["tags"]))
MEDIA_TYPES = ["book", "movie", "song"]
LANGUAGES = ["en", "it", "hi"]
