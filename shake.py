import tkinter as tk
from tkinter import ttk, messagebox
import random
import threading
import time
import base64
from io import BytesIO

class ModernShakespeareApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎭 Shakespeare Multiverse")
        self.root.geometry("1000x800")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(True, True)
        
        # Fixed color scheme
        self.colors = {
            'bg': '#1a1a2e',           # Deep navy background
            'card_bg': '#16213e',      # Darker card background
            'accent': '#e94560',       # Bright red accent
            'text': '#ffffff',         # Pure white text
            'secondary': '#a0a0a0',    # Light gray secondary
            'gold': '#f39c12',         # Warm gold
            'success': '#27ae60',      # Green for success
            'button_hover': '#c0392b', # Darker red for hover
            'border': '#34495e'        # Subtle border color
        }
        
        # Expanded quotes with play sources
        self.quotes = {
            'English': [
                {"quote": "To be or not to be, that is the question.", "source": "Hamlet, Act 3, Scene 1"},
                {"quote": "All the world's a stage, and all the men and women merely players.", "source": "As You Like It, Act 2, Scene 7"},
                {"quote": "What's in a name? That which we call a rose by any other name would smell as sweet.", "source": "Romeo and Juliet, Act 2, Scene 2"},
                {"quote": "The course of true love never did run smooth.", "source": "A Midsummer Night's Dream, Act 1, Scene 1"},
                {"quote": "Neither a borrower nor a lender be.", "source": "Hamlet, Act 1, Scene 3"}
            ],
            'Spanish': [
                {"quote": "Ser o no ser, esa es la cuestión.", "source": "Hamlet, Acto 3, Escena 1"},
                {"quote": "Todo el mundo es un escenario, y todos los hombres y mujeres simplemente actores.", "source": "Como Gustéis, Acto 2, Escena 7"},
                {"quote": "¿Qué hay en un nombre? Lo que llamamos rosa con cualquier otro nombre olería igual de dulce.", "source": "Romeo y Julieta, Acto 2, Escena 2"},
                {"quote": "El curso del amor verdadero nunca fue suave.", "source": "Sueño de una Noche de Verano, Acto 1, Escena 1"},
                {"quote": "Ni prestamista ni prestatario seas.", "source": "Hamlet, Acto 1, Escena 3"}
            ],
            'French': [
                {"quote": "Être ou ne pas être, telle est la question.", "source": "Hamlet, Acte 3, Scène 1"},
                {"quote": "Le monde entier est une scène, et tous les hommes et femmes ne sont que des acteurs.", "source": "Comme il vous plaira, Acte 2, Scène 7"},
                {"quote": "Qu'y a-t-il dans un nom? Ce que nous appelons rose sentirait aussi bon sous un autre nom.", "source": "Roméo et Juliette, Acte 2, Scène 2"},
                {"quote": "Le cours du vrai amour n'a jamais été fluide.", "source": "Le Songe d'une nuit d'été, Acte 1, Scène 1"},
                {"quote": "Ne sois ni emprunteur ni prêteur.", "source": "Hamlet, Acte 1, Scène 3"}
            ],
            'German': [
                {"quote": "Sein oder nicht sein, das ist die Frage.", "source": "Hamlet, 3. Akt, 1. Szene"},
                {"quote": "Die ganze Welt ist eine Bühne, und alle Männer und Frauen sind nur Spieler.", "source": "Wie es euch gefällt, 2. Akt, 7. Szene"},
                {"quote": "Was ist in einem Namen? Was wir Rose nennen, würde unter jedem anderen Namen genauso süß riechen.", "source": "Romeo und Julia, 2. Akt, 2. Szene"},
                {"quote": "Der Verlauf wahrer Liebe war nie glatt.", "source": "Ein Sommernachtstraum, 1. Akt, 1. Szene"},
                {"quote": "Weder Borger noch Verleiher sei.", "source": "Hamlet, 1. Akt, 3. Szene"}
            ],
            'Italian': [
                {"quote": "Essere o non essere, questa è la domanda.", "source": "Amleto, Atto 3, Scena 1"},
                {"quote": "Tutto il mondo è un palcoscenico, e tutti gli uomini e le donne sono semplicemente attori.", "source": "Come vi piace, Atto 2, Scena 7"},
                {"quote": "Cosa c'è in un nome? Quello che chiamiamo rosa con qualsiasi altro nome profumerebbe altrettanto dolce.", "source": "Romeo e Giulietta, Atto 2, Scena 2"},
                {"quote": "Il corso del vero amore non è mai stato liscio.", "source": "Sogno di una notte di mezza estate, Atto 1, Scena 1"},
                {"quote": "Non essere né mutuatario né prestatore.", "source": "Amleto, Atto 1, Scena 3"}
            ],
            'Japanese': [
                {"quote": "生きるべきか死ぬべきか、それが問題だ。", "source": "ハムレット、第3幕第1場"},
                {"quote": "全世界は舞台であり、すべての男女は単なる役者に過ぎない。", "source": "お気に召すまま、第2幕第7場"},
                {"quote": "名前に何があるのか？バラと呼ぶものは、他のどんな名前でも同じように甘い香りがするだろう。", "source": "ロミオとジュリエット、第2幕第2場"},
                {"quote": "真の愛の道のりは決して滑らかではなかった。", "source": "真夏の夜の夢、第1幕第1場"},
                {"quote": "借りる者にも貸す者にもなるな。", "source": "ハムレット、第1幕第3場"}
            ],
            'Chinese': [
                {"quote": "生存还是毁灭，这是个问题。", "source": "哈姆雷特，第三幕第一场"},
                {"quote": "整个世界是一个舞台，所有的男男女女不过是演员。", "source": "皆大欢喜，第二幕第七场"},
                {"quote": "名字里有什么？我们称之为玫瑰的东西，换个名字还是一样香甜。", "source": "罗密欧与朱丽叶，第二幕第二场"},
                {"quote": "真爱的道路从来都不平坦。", "source": "仲夏夜之梦，第一幕第一场"},
                {"quote": "既不借贷，也不放贷。", "source": "哈姆雷特，第一幕第三场"}
            ],
            'Russian': [
                {"quote": "Быть или не быть, вот в чём вопрос.", "source": "Гамлет, Акт 3, Сцена 1"},
                {"quote": "Весь мир — театр, а люди в нём — актёры.", "source": "Как вам это понравится, Акт 2, Сцена 7"},
                {"quote": "Что в имени? То, что мы зовём розой, пахло бы так же сладко под любым другим именем.", "source": "Ромео и Джульетта, Акт 2, Сцена 2"},
                {"quote": "Путь истинной любви никогда не был гладким.", "source": "Сон в летнюю ночь, Акт 1, Сцена 1"},
                {"quote": "Ни заёмщиком, ни кредитором не будь.", "source": "Гамлет, Акт 1, Сцена 3"}
            ]
        }
        
        self.current_quote_index = 0
        self.current_language = 'English'
        self.typing_active = False
        self.favorites = []
        
        self.create_shakespeare_image()
        self.create_modern_ui()
        
    def create_shakespeare_image(self):
        """Create ASCII art representation of Shakespeare"""
        self.shakespeare_ascii = """
    ⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
    ⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀
    ⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
    ⠀⠀⣿⣿⣿⡿⢛⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⡛⢿⣿⣿⣿⠀⠀
    ⠀⢸⣿⣿⡿⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⡇⠀
    ⠀⣾⣿⣿⠃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠘⣿⣿⣷⠀
    ⢠⣿⣿⡏⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⣿⣿⡄
    ⣸⣿⣿⠁⣿⣿⣿⣿⡿⠛⠛⠛⠛⠛⢿⣿⣿⣿⣿⣿⠈⣿⣿⣇
    ⣿⣿⡇⢠⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⡄⢸⣿⣿
    ⣿⣿⡇⢸⣿⣿⣿⠁⠀⣤⣤⣤⣤⣤⠀⠈⣿⣿⣿⣿⡇⢸⣿⣿
    ⣿⣿⣿⠘⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⠃⣿⣿⣿
    ⢹⣿⣿⡄⢻⣿⣿⡄⠀⠙⠿⠿⠿⠋⠀⢠⣿⣿⡿⢁⣿⣿⡏
    ⠀⢻⣿⣿⣆⠙⢿⣿⣷⣤⣀⣀⣀⣤⣾⣿⡿⠋⣰⣿⣿⡟⠀
    ⠀⠀⠻⣿⣿⣷⣄⠉⠛⠿⠿⠿⠿⠛⠉⣠⣾⣿⣿⠟⠀⠀
    ⠀⠀⠀⠈⠻⣿⣿⣿⣶⣤⣤⣤⣤⣶⣿⣿⣿⠟⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀
    """
    
    def create_modern_ui(self):
        """Create improved modern UI"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Header section
        header_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        header_frame.pack(fill='x', pady=(0, 20))
        
        # Title
        title_label = tk.Label(header_frame, 
                              text="🎭 SHAKESPEARE MULTIVERSE 🎭",
                              font=('Helvetica', 26, 'bold'),
                              fg=self.colors['gold'],
                              bg=self.colors['bg'])
        title_label.pack()
        
        subtitle_label = tk.Label(header_frame,
                                 text="Experience the Bard's wisdom across cultures",
                                 font=('Helvetica', 12, 'italic'),
                                 fg=self.colors['secondary'],
                                 bg=self.colors['bg'])
        subtitle_label.pack(pady=(5, 0))
        
        # Main content area
        content_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        content_frame.pack(fill='both', expand=True)
        
        # Left side - Shakespeare portrait
        left_frame = tk.Frame(content_frame, bg=self.colors['bg'])
        left_frame.pack(side='left', fill='y', padx=(0, 20))
        
        # Shakespeare ASCII art
        portrait_frame = tk.Frame(left_frame, bg=self.colors['card_bg'], relief='solid', bd=2)
        portrait_frame.pack(pady=(0, 20))
        
        shakespeare_label = tk.Label(portrait_frame,
                                   text=self.shakespeare_ascii,
                                   font=('Courier', 8),
                                   fg=self.colors['gold'],
                                   bg=self.colors['card_bg'],
                                   justify='center')
        shakespeare_label.pack(padx=10, pady=10)
        
        # Shakespeare info
        info_label = tk.Label(left_frame,
                             text="William Shakespeare\n(1564-1616)\n\n\"The Bard of Avon\"",
                             font=('Helvetica', 11, 'italic'),
                             fg=self.colors['text'],
                             bg=self.colors['bg'],
                             justify='center')
        info_label.pack()
        
        # Statistics
        stats_frame = tk.Frame(left_frame, bg=self.colors['card_bg'], relief='solid', bd=1)
        stats_frame.pack(fill='x', pady=(20, 0))
        
        stats_title = tk.Label(stats_frame,
                              text="📊 Your Stats",
                              font=('Helvetica', 12, 'bold'),
                              fg=self.colors['accent'],
                              bg=self.colors['card_bg'])
        stats_title.pack(pady=(10, 5))
        
        self.stats_var = tk.StringVar(value="Quotes viewed: 0\nLanguages explored: 1\nFavorites saved: 0")
        stats_label = tk.Label(stats_frame,
                              textvariable=self.stats_var,
                              font=('Helvetica', 10),
                              fg=self.colors['text'],
                              bg=self.colors['card_bg'],
                              justify='left')
        stats_label.pack(padx=10, pady=(0, 10))
        
        # Right side - Quote display
        right_frame = tk.Frame(content_frame, bg=self.colors['bg'])
        right_frame.pack(side='right', fill='both', expand=True)
        
        # Quote card
        quote_card = tk.Frame(right_frame, bg=self.colors['card_bg'], relief='solid', bd=2)
        quote_card.pack(fill='x', pady=(0, 20))
        
        # Quote text
        self.quote_label = tk.Label(quote_card,
                                   text=self.quotes[self.current_language][0]['quote'],
                                   font=('Georgia', 16, 'italic'),
                                   fg=self.colors['text'],
                                   bg=self.colors['card_bg'],
                                   wraplength=600,
                                   justify='center',
                                   pady=30,
                                   padx=20)
        self.quote_label.pack(fill='x')
        
        # Source info
        self.source_label = tk.Label(quote_card,
                                    text=self.quotes[self.current_language][0]['source'],
                                    font=('Helvetica', 10, 'italic'),
                                    fg=self.colors['secondary'],
                                    bg=self.colors['card_bg'])
        self.source_label.pack(pady=(0, 10))
        
        # Language info
        self.lang_info = tk.Label(quote_card,
                                 text=f"— {self.current_language} —",
                                 font=('Helvetica', 12, 'bold'),
                                 fg=self.colors['accent'],
                                 bg=self.colors['card_bg'])
        self.lang_info.pack(pady=(0, 20))
        
        # Control buttons
        controls_frame = tk.Frame(right_frame, bg=self.colors['bg'])
        controls_frame.pack(fill='x', pady=(0, 20))
        
        # First row of buttons
        btn_row1 = tk.Frame(controls_frame, bg=self.colors['bg'])
        btn_row1.pack(fill='x', pady=(0, 10))
        
        self.create_button(btn_row1, "🎲 Random Quote", self.random_quote, self.colors['accent'], 'left')
        self.create_button(btn_row1, "⌨️ Typewriter", self.toggle_typewriter, self.colors['gold'], 'left', fg='black')
        self.create_button(btn_row1, "➡️ Next Quote", self.next_quote, self.colors['success'], 'right')
        
        # Second row of buttons
        btn_row2 = tk.Frame(controls_frame, bg=self.colors['bg'])
        btn_row2.pack(fill='x')
        
        self.create_button(btn_row2, "❤️ Favorite", self.add_favorite, '#e74c3c', 'left')
        self.create_button(btn_row2, "📋 View Favorites", self.show_favorites, '#9b59b6', 'left')
        self.create_button(btn_row2, "🔄 Reset Stats", self.reset_stats, '#34495e', 'right')
        
        # Language selection
        self.create_language_section(right_frame)
        
        # Status bar
        self.status_var = tk.StringVar(value="Welcome to Shakespeare's Multiverse! Select a language to begin.")
        status_bar = tk.Label(main_frame,
                             textvariable=self.status_var,
                             font=('Helvetica', 10),
                             fg=self.colors['secondary'],
                             bg=self.colors['bg'],
                             relief='sunken',
                             bd=1)
        status_bar.pack(side='bottom', fill='x', pady=(15, 0))
        
        self.quotes_viewed = 0
        self.languages_explored = set(['English'])
        
    def create_button(self, parent, text, command, bg_color, side, fg='white'):
        """Helper to create consistent buttons"""
        btn = tk.Button(parent,
                       text=text,
                       command=command,
                       bg=bg_color,
                       fg=fg,
                       font=('Helvetica', 10, 'bold'),
                       relief='flat',
                       padx=15,
                       pady=8,
                       cursor='hand2',
                       activebackground=self.colors['button_hover'] if bg_color == self.colors['accent'] else bg_color,
                       activeforeground=fg)
        btn.pack(side=side, padx=5)
        
        # Hover effects
        def on_enter(e):
            btn.config(bg=self.colors['button_hover'] if bg_color == self.colors['accent'] else bg_color)
        def on_leave(e):
            btn.config(bg=bg_color)
            
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
    def create_language_section(self, parent):
        """Create improved language selection"""
        lang_frame = tk.Frame(parent, bg=self.colors['bg'])
        lang_frame.pack(fill='x')
        
        lang_title = tk.Label(lang_frame,
                             text="🌍 Choose Your Language:",
                             font=('Helvetica', 14, 'bold'),
                             fg=self.colors['text'],
                             bg=self.colors['bg'])
        lang_title.pack(pady=(0, 15))
        
        # Language buttons in a cleaner grid
        button_frame = tk.Frame(lang_frame, bg=self.colors['bg'])
        button_frame.pack()
        
        languages = list(self.quotes.keys())
        lang_colors = {
            'English': '#3498db',
            'Spanish': '#e74c3c', 
            'French': '#9b59b6',
            'German': '#f39c12',
            'Italian': '#27ae60',
            'Japanese': '#e67e22',
            'Chinese': '#c0392b',
            'Russian': '#8e44ad'
        }
        
        for i, lang in enumerate(languages):
            row = i // 4
            col = i % 4
            
            color = lang_colors.get(lang, self.colors['accent'])
            
            btn = tk.Button(button_frame,
                           text=f"🌍 {lang}",
                           command=lambda l=lang: self.change_language(l),
                           bg=color,
                           fg='white',
                           font=('Helvetica', 10, 'bold'),
                           relief='flat',
                           padx=20,
                           pady=10,
                           cursor='hand2',
                           width=12)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='ew')
            
            # Hover effects
            def make_hover_funcs(button, original_color):
                def on_enter(e):
                    button.config(bg=self.colors['button_hover'])
                def on_leave(e):
                    button.config(bg=original_color)
                return on_enter, on_leave
            
            enter_func, leave_func = make_hover_funcs(btn, color)
            btn.bind("<Enter>", enter_func)
            btn.bind("<Leave>", leave_func)
            
            button_frame.grid_columnconfigure(col, weight=1)
        
    def change_language(self, language):
        """Change language with improved feedback"""
        self.current_language = language
        self.current_quote_index = 0
        self.languages_explored.add(language)
        
        quote_data = self.quotes[language][self.current_quote_index]
        
        # Smooth transition effect
        self.quote_label.config(fg=self.colors['secondary'])
        self.root.update()
        time.sleep(0.1)
        
        self.quote_label.config(text=quote_data['quote'], fg=self.colors['text'])
        self.source_label.config(text=quote_data['source'])
        self.lang_info.config(text=f"— {language} —")
        
        self.update_stats()
        self.status_var.set(f"Switched to {language}! {len(self.quotes[language])} quotes available.")
        
    def next_quote(self):
        """Show next quote with source info"""
        quotes_in_lang = self.quotes[self.current_language]
        self.current_quote_index = (self.current_quote_index + 1) % len(quotes_in_lang)
        
        quote_data = quotes_in_lang[self.current_quote_index]
        self.quote_label.config(text=quote_data['quote'])
        self.source_label.config(text=quote_data['source'])
        
        self.quotes_viewed += 1
        self.update_stats()
        self.status_var.set(f"Quote {self.current_quote_index + 1} of {len(quotes_in_lang)} in {self.current_language}")
        
    def random_quote(self):
        """Enhanced random quote selection"""
        random_lang = random.choice(list(self.quotes.keys()))
        quote_data = random.choice(self.quotes[random_lang])
        
        self.current_language = random_lang
        self.current_quote_index = self.quotes[random_lang].index(quote_data)
        self.languages_explored.add(random_lang)
        
        self.quote_label.config(text=quote_data['quote'])
        self.source_label.config(text=quote_data['source'])
        self.lang_info.config(text=f"— {random_lang} —")
        
        self.quotes_viewed += 1
        self.update_stats()
        self.status_var.set(f"Random selection: {random_lang} - {quote_data['source']}")
        
    def add_favorite(self):
        """Add current quote to favorites"""
        current_quote = self.quotes[self.current_language][self.current_quote_index]
        favorite_entry = {
            'quote': current_quote['quote'],
            'source': current_quote['source'],
            'language': self.current_language
        }
        
        if favorite_entry not in self.favorites:
            self.favorites.append(favorite_entry)
            self.status_var.set("Quote added to favorites! ❤️")
            self.update_stats()
        else:
            self.status_var.set("Quote already in favorites!")
            
    def show_favorites(self):
        """Display favorites in a popup window"""
        if not self.favorites:
            messagebox.showinfo("Favorites", "No favorite quotes saved yet!\nClick the ❤️ button to save quotes.")
            return
            
        favorites_window = tk.Toplevel(self.root)
        favorites_window.title("Your Favorite Quotes")
        favorites_window.geometry("600x400")
        favorites_window.configure(bg=self.colors['bg'])
        
        # Scrollable text area
        text_frame = tk.Frame(favorites_window, bg=self.colors['bg'])
        text_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        text_area = tk.Text(text_frame, 
                           bg=self.colors['card_bg'],
                           fg=self.colors['text'],
                           font=('Georgia', 12),
                           wrap='word',
                           padx=15,
                           pady=15)
        
        scrollbar = tk.Scrollbar(text_frame, command=text_area.yview)
        text_area.config(yscrollcommand=scrollbar.set)
        
        text_area.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Populate favorites
        for i, fav in enumerate(self.favorites, 1):
            text_area.insert('end', f"{i}. \"{fav['quote']}\"\n")
            text_area.insert('end', f"   — {fav['source']} ({fav['language']})\n\n")
            
        text_area.config(state='disabled')
        
    def reset_stats(self):
        """Reset all statistics"""
        result = messagebox.askyesno("Reset Statistics", 
                                   "Are you sure you want to reset all statistics?\nThis will clear your view count but keep your favorites.")
        if result:
            self.quotes_viewed = 0
            self.languages_explored = set([self.current_language])
            self.update_stats()
            self.status_var.set("Statistics reset successfully!")
            
    def update_stats(self):
        """Update statistics display"""
        stats_text = f"Quotes viewed: {self.quotes_viewed}\nLanguages explored: {len(self.languages_explored)}\nFavorites saved: {len(self.favorites)}"
        self.stats_var.set(stats_text)
        
    def typewriter_effect(self, text):
        """Enhanced typewriter effect"""
        self.typing_active = True
        self.quote_label.config(text="", fg=self.colors['gold'])
        
        for i in range(len(text) + 1):
            if not self.typing_active:
                break
            display_text = text[:i]
            if i < len(text):
                display_text += "▌"  # Block cursor
            self.quote_label.config(text=display_text)
            self.root.update()
            time.sleep(0.03)
            
        if self.typing_active:
            self.quote_label.config(text=text, fg=self.colors['text'])
        self.typing_active = False
        
    def toggle_typewriter(self):
        """Toggle typewriter effect for current quote"""
        if not self.typing_active:
            current_quote = self.quotes[self.current_language][self.current_quote_index]['quote']
            threading.Thread(target=self.typewriter_effect, args=(current_quote,), daemon=True).start()
            self.status_var.set("Typewriter effect activated... ⌨️")
        else:
            self.typing_active = False
            self.status_var.set("Typewriter effect stopped.")
            
    def run(self):
        """Start the application with fade-in effect"""
        # Startup animation
        self.root.attributes('-alpha', 0.0)
        
        def fade_in():
            alpha = 0.0
            while alpha < 1.0:
                alpha += 0.02
                try:
                    self.root.attributes('-alpha', alpha)
                    self.root.update()
                    time.sleep(0.01)
                except:
                    break
                    
        # Start fade-in after a brief delay
        self.root.after(50, fade_in)
        
        # Welcome message
        self.root.after(1000, lambda: self.status_var.set("Welcome to Shakespeare's Multiverse! Click any language to explore."))
        
        self.root.mainloop()

if __name__ == "__main__":
    app = ModernShakespeareApp()
    app.run()