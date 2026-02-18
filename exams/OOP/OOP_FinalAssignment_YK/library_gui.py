"""
Library Management System - Interactive GUI
A graphical user interface for testing the Library Management System

This GUI allows students to interactively test all features:
- Add/view books and members
- Borrow and return books
- Search functionality
- View transactions
- Test iterators and generators
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime
import sys

# Import all the library system modules
from library_items import Book, EBook, AudioBook, PhysicalBook
from members import Member, StudentMember, PremiumMember
from library import Library
from book_collection import BookCollection
import config
import utils


class LibraryGUI:
    """Main GUI Application for Library Management System."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System - Interactive Testing Interface")
        self.root.geometry("1200x800")
        self.root.configure(bg="#86aed6")
        
        # Initialize library
        self.library = Library(config.LIBRARY_NAME)
        
        # Add some sample data
        self._add_sample_data()
        
        # Create GUI components
        self._create_menu()
        self._create_main_layout()
        self._create_status_bar()
        
        # Refresh displays
        self.refresh_all()
    
    def _add_sample_data(self):
        """Add sample books and members for testing."""
        # Sample books
        self.library.add_book(PhysicalBook("1984", "George Orwell", "978-0451524935", 1949, "A-1", "Good"))
        self.library.add_book(PhysicalBook("To Kill a Mockingbird", "Harper Lee", "978-0061120084", 1960, "A-2", "Excellent"))
        self.library.add_book(EBook("Python Crash Course", "Eric Matthes", "978-1593279288", 2019, 8.5, "PDF"))
        self.library.add_book(EBook("Clean Code", "Robert Martin", "978-0132350884", 2008, 6.2, "EPUB"))
        self.library.add_book(AudioBook("Atomic Habits", "James Clear", "978-0735211292", 2018, "Various", 320))
        
        # Sample members (don't print to GUI)
        import io
        import contextlib
        
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.library.add_member(Member("Alice Johnson", "M001", "alice@email.com"))
            self.library.add_member(StudentMember("Bob Smith", "M002", "bob@university.edu", "S12345", "MIT"))
            self.library.add_member(PremiumMember("Carol White", "M003", "carol@email.com", "2026-12-31"))
    
    def _create_menu(self):
        """Create menu bar."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Refresh All", command=self.refresh_all)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
    
    def _create_main_layout(self):
        """Create main layout with notebook tabs."""
        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create tabs
        self.tab_books = ttk.Frame(self.notebook)
        self.tab_members = ttk.Frame(self.notebook)
        self.tab_transactions = ttk.Frame(self.notebook)
        self.tab_search = ttk.Frame(self.notebook)
        self.tab_advanced = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_books, text="📚 Books")
        self.notebook.add(self.tab_members, text="👥 Members")
        self.notebook.add(self.tab_transactions, text="📝 Transactions")
        self.notebook.add(self.tab_search, text="🔍 Search")
        self.notebook.add(self.tab_advanced, text="⚙️ Advanced Features")
        
        # Setup each tab
        self._setup_books_tab()
        self._setup_members_tab()
        self._setup_transactions_tab()
        self._setup_search_tab()
        self._setup_advanced_tab()
    
    def _setup_books_tab(self):
        """Setup books management tab."""
        # Left panel - Book list
        left_frame = ttk.LabelFrame(self.tab_books, text="Available Books", padding=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Treeview for books
        columns = ("Title", "Author", "Type", "ISBN", "Available")
        self.books_tree = ttk.Treeview(left_frame, columns=columns, show="tree headings", height=20)
        
        self.books_tree.heading("#0", text="ID")
        self.books_tree.column("#0", width=50)
        for col in columns:
            self.books_tree.heading(col, text=col)
            self.books_tree.column(col, width=150)
        
        scrollbar = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=self.books_tree.yview)
        self.books_tree.configure(yscrollcommand=scrollbar.set)
        
        self.books_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Right panel - Add book
        right_frame = ttk.LabelFrame(self.tab_books, text="Add New Book", padding=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=5, pady=5)
        
        # Book type selection
        ttk.Label(right_frame, text="Book Type:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.book_type_var = tk.StringVar(value="Physical")
        book_types = ttk.Combobox(right_frame, textvariable=self.book_type_var, 
                                   values=["Physical", "EBook", "AudioBook"], state="readonly", width=25)
        book_types.grid(row=0, column=1, pady=5)
        book_types.bind("<<ComboboxSelected>>", self._on_book_type_change)
        
        # Common fields
        ttk.Label(right_frame, text="Title:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.book_title_var = tk.StringVar()
        ttk.Entry(right_frame, textvariable=self.book_title_var, width=27).grid(row=1, column=1, pady=5)
        
        ttk.Label(right_frame, text="Author:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.book_author_var = tk.StringVar()
        ttk.Entry(right_frame, textvariable=self.book_author_var, width=27).grid(row=2, column=1, pady=5)
        
        ttk.Label(right_frame, text="ISBN:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.book_isbn_var = tk.StringVar()
        ttk.Entry(right_frame, textvariable=self.book_isbn_var, width=27).grid(row=3, column=1, pady=5)
        
        ttk.Label(right_frame, text="Year:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.book_year_var = tk.StringVar()
        ttk.Entry(right_frame, textvariable=self.book_year_var, width=27).grid(row=4, column=1, pady=5)
        
        # Type-specific fields frame
        self.book_specific_frame = ttk.Frame(right_frame)
        self.book_specific_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        self._create_physical_book_fields()
        
        # Add button
        ttk.Button(right_frame, text="Add Book", command=self.add_book, width=27).grid(row=6, column=0, columnspan=2, pady=10)
        
        # Book details button
        ttk.Button(right_frame, text="View Selected Book Details", command=self.view_book_details, width=27).grid(row=7, column=0, columnspan=2, pady=5)
    
    def _on_book_type_change(self, event=None):
        """Handle book type change."""
        # Clear specific frame
        for widget in self.book_specific_frame.winfo_children():
            widget.destroy()
        
        book_type = self.book_type_var.get()
        if book_type == "Physical":
            self._create_physical_book_fields()
        elif book_type == "EBook":
            self._create_ebook_fields()
        elif book_type == "AudioBook":
            self._create_audiobook_fields()
    
    def _create_physical_book_fields(self):
        """Create fields specific to physical books."""
        ttk.Label(self.book_specific_frame, text="Shelf Location:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.shelf_var = tk.StringVar(value="A-1")
        ttk.Entry(self.book_specific_frame, textvariable=self.shelf_var, width=27).grid(row=0, column=1, pady=5)
        
        ttk.Label(self.book_specific_frame, text="Condition:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.condition_var = tk.StringVar(value="Good")
        ttk.Combobox(self.book_specific_frame, textvariable=self.condition_var, 
                     values=["New", "Excellent", "Good", "Fair", "Poor"], state="readonly", width=25).grid(row=1, column=1, pady=5)
    
    def _create_ebook_fields(self):
        """Create fields specific to ebooks."""
        ttk.Label(self.book_specific_frame, text="File Size (MB):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.filesize_var = tk.StringVar(value="5.0")
        ttk.Entry(self.book_specific_frame, textvariable=self.filesize_var, width=27).grid(row=0, column=1, pady=5)
        
        ttk.Label(self.book_specific_frame, text="Format:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.format_var = tk.StringVar(value="PDF")
        ttk.Combobox(self.book_specific_frame, textvariable=self.format_var, 
                     values=["PDF", "EPUB", "MOBI", "AZW"], state="readonly", width=25).grid(row=1, column=1, pady=5)
    
    def _create_audiobook_fields(self):
        """Create fields specific to audiobooks."""
        ttk.Label(self.book_specific_frame, text="Narrator:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.narrator_var = tk.StringVar()
        ttk.Entry(self.book_specific_frame, textvariable=self.narrator_var, width=27).grid(row=0, column=1, pady=5)
        
        ttk.Label(self.book_specific_frame, text="Duration (min):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.duration_var = tk.StringVar(value="180")
        ttk.Entry(self.book_specific_frame, textvariable=self.duration_var, width=27).grid(row=1, column=1, pady=5)
    
    def _setup_members_tab(self):
        """Setup members management tab."""
        # Left panel - Member list
        left_frame = ttk.LabelFrame(self.tab_members, text="Library Members", padding=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Treeview for members
        columns = ("Name", "ID", "Email", "Type", "Books", "Max")
        self.members_tree = ttk.Treeview(left_frame, columns=columns, show="tree headings", height=20)
        
        self.members_tree.heading("#0", text="")
        self.members_tree.column("#0", width=30)
        for col in columns:
            self.members_tree.heading(col, text=col)
            self.members_tree.column(col, width=120)
        
        scrollbar = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=self.members_tree.yview)
        self.members_tree.configure(yscrollcommand=scrollbar.set)
        
        self.members_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Right panel - Add member
        right_frame = ttk.LabelFrame(self.tab_members, text="Add New Member", padding=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=5, pady=5)
        
        # Member type selection
        ttk.Label(right_frame, text="Member Type:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.member_type_var = tk.StringVar(value="Regular")
        member_types = ttk.Combobox(right_frame, textvariable=self.member_type_var, 
                                     values=["Regular", "Student", "Premium"], state="readonly", width=25)
        member_types.grid(row=0, column=1, pady=5)
        member_types.bind("<<ComboboxSelected>>", self._on_member_type_change)
        
        # Common fields
        ttk.Label(right_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.member_name_var = tk.StringVar()
        ttk.Entry(right_frame, textvariable=self.member_name_var, width=27).grid(row=1, column=1, pady=5)
        
        ttk.Label(right_frame, text="Member ID:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.member_id_var = tk.StringVar()
        ttk.Entry(right_frame, textvariable=self.member_id_var, width=27).grid(row=2, column=1, pady=5)
        
        ttk.Label(right_frame, text="Email:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.member_email_var = tk.StringVar()
        ttk.Entry(right_frame, textvariable=self.member_email_var, width=27).grid(row=3, column=1, pady=5)
        
        # Generate ID button
        ttk.Button(right_frame, text="Generate ID", command=self.generate_member_id, width=27).grid(row=4, column=0, columnspan=2, pady=5)
        
        # Type-specific fields frame
        self.member_specific_frame = ttk.Frame(right_frame)
        self.member_specific_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Add button
        ttk.Button(right_frame, text="Add Member", command=self.add_member, width=27).grid(row=6, column=0, columnspan=2, pady=10)
        
        # Member details button
        ttk.Button(right_frame, text="View Selected Member Details", command=self.view_member_details, width=27).grid(row=7, column=0, columnspan=2, pady=5)
    
    def _on_member_type_change(self, event=None):
        """Handle member type change."""
        # Clear specific frame
        for widget in self.member_specific_frame.winfo_children():
            widget.destroy()
        
        member_type = self.member_type_var.get()
        if member_type == "Student":
            self._create_student_fields()
        elif member_type == "Premium":
            self._create_premium_fields()
    
    def _create_student_fields(self):
        """Create fields specific to student members."""
        ttk.Label(self.member_specific_frame, text="Student ID:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.student_id_var = tk.StringVar()
        ttk.Entry(self.member_specific_frame, textvariable=self.student_id_var, width=27).grid(row=0, column=1, pady=5)
        
        ttk.Label(self.member_specific_frame, text="University:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.university_var = tk.StringVar()
        ttk.Entry(self.member_specific_frame, textvariable=self.university_var, width=27).grid(row=1, column=1, pady=5)
    
    def _create_premium_fields(self):
        """Create fields specific to premium members."""
        ttk.Label(self.member_specific_frame, text="Expiry Date:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.expiry_var = tk.StringVar(value="2026-12-31")
        ttk.Entry(self.member_specific_frame, textvariable=self.expiry_var, width=27).grid(row=0, column=1, pady=5)
        ttk.Label(self.member_specific_frame, text="(Format: YYYY-MM-DD)", font=("Arial", 8)).grid(row=1, column=0, columnspan=2)
    
    def _setup_transactions_tab(self):
        """Setup transactions management tab."""
        # Top frame - Actions
        top_frame = ttk.LabelFrame(self.tab_transactions, text="Borrow / Return Books", padding=10)
        top_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Borrow section
        borrow_frame = ttk.Frame(top_frame)
        borrow_frame.pack(side=tk.LEFT, padx=20)
        
        ttk.Label(borrow_frame, text="Member ID:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.borrow_member_var = tk.StringVar()
        ttk.Entry(borrow_frame, textvariable=self.borrow_member_var, width=15).grid(row=0, column=1, pady=2)
        
        ttk.Label(borrow_frame, text="Book ISBN:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.borrow_isbn_var = tk.StringVar()
        ttk.Entry(borrow_frame, textvariable=self.borrow_isbn_var, width=15).grid(row=1, column=1, pady=2)
        
        ttk.Label(borrow_frame, text="Date:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.borrow_date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        ttk.Entry(borrow_frame, textvariable=self.borrow_date_var, width=15).grid(row=2, column=1, pady=2)
        
        ttk.Button(borrow_frame, text="Borrow Book", command=self.borrow_book).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Return section
        return_frame = ttk.Frame(top_frame)
        return_frame.pack(side=tk.LEFT, padx=20)
        
        ttk.Label(return_frame, text="Member ID:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.return_member_var = tk.StringVar()
        ttk.Entry(return_frame, textvariable=self.return_member_var, width=15).grid(row=0, column=1, pady=2)
        
        ttk.Label(return_frame, text="Book ISBN:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.return_isbn_var = tk.StringVar()
        ttk.Entry(return_frame, textvariable=self.return_isbn_var, width=15).grid(row=1, column=1, pady=2)
        
        ttk.Label(return_frame, text="Return Date:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.return_date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        ttk.Entry(return_frame, textvariable=self.return_date_var, width=15).grid(row=2, column=1, pady=2)
        
        ttk.Button(return_frame, text="Return Book", command=self.return_book).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Bottom frame - Transaction list
        bottom_frame = ttk.LabelFrame(self.tab_transactions, text="Transaction History", padding=10)
        bottom_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Treeview for transactions
        columns = ("ID", "Member", "Book", "Borrow Date", "Return Date", "Status")
        self.trans_tree = ttk.Treeview(bottom_frame, columns=columns, show="tree headings", height=15)
        
        self.trans_tree.heading("#0", text="")
        self.trans_tree.column("#0", width=30)
        for col in columns:
            self.trans_tree.heading(col, text=col)
            self.trans_tree.column(col, width=150)
        
        scrollbar = ttk.Scrollbar(bottom_frame, orient=tk.VERTICAL, command=self.trans_tree.yview)
        self.trans_tree.configure(yscrollcommand=scrollbar.set)
        
        self.trans_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Refresh button
        ttk.Button(bottom_frame, text="Refresh Transactions", command=self.refresh_transactions).pack(pady=5)
    
    def _setup_search_tab(self):
        """Setup search functionality tab."""
        # Search frame
        search_frame = ttk.LabelFrame(self.tab_search, text="Search Library", padding=10)
        search_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(search_frame, text="Search Term:").pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.search_var, width=40).pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Search Books & Members", command=self.search_library).pack(side=tk.LEFT, padx=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(self.tab_search, text="Search Results", padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.search_results = scrolledtext.ScrolledText(results_frame, width=100, height=30, wrap=tk.WORD)
        self.search_results.pack(fill=tk.BOTH, expand=True)
    
    def _setup_advanced_tab(self):
        """Setup advanced features tab."""
        # Iterator test frame
        iter_frame = ttk.LabelFrame(self.tab_advanced, text="Test Iterators", padding=10)
        iter_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(iter_frame, text="Iterate Through All Books", command=self.test_iterator).pack(side=tk.LEFT, padx=5)
        ttk.Button(iter_frame, text="Show Available Books", command=self.test_available_books).pack(side=tk.LEFT, padx=5)
        
        # Generator test frame
        gen_frame = ttk.LabelFrame(self.tab_advanced, text="Test Generators", padding=10)
        gen_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(gen_frame, text="Author:").pack(side=tk.LEFT, padx=5)
        self.author_search_var = tk.StringVar()
        ttk.Entry(gen_frame, textvariable=self.author_search_var, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(gen_frame, text="Find Books by Author", command=self.test_books_by_author).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(gen_frame, text="Type:").pack(side=tk.LEFT, padx=5)
        self.type_search_var = tk.StringVar(value="EBook")
        ttk.Combobox(gen_frame, textvariable=self.type_search_var, 
                     values=["Book", "EBook", "AudioBook", "PhysicalBook"], width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(gen_frame, text="Find Books by Type", command=self.test_books_by_type).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(gen_frame, text="Show Active Members", command=self.test_active_members).pack(side=tk.LEFT, padx=5)
        
        # Utilities test frame
        util_frame = ttk.LabelFrame(self.tab_advanced, text="Test Utility Functions", padding=10)
        util_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(util_frame, text="Validate Email", command=self.test_email_validation).pack(side=tk.LEFT, padx=5)
        ttk.Button(util_frame, text="Validate ISBN", command=self.test_isbn_validation).pack(side=tk.LEFT, padx=5)
        ttk.Button(util_frame, text="Calculate Date Difference", command=self.test_date_calc).pack(side=tk.LEFT, padx=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(self.tab_advanced, text="Test Results", padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.advanced_results = scrolledtext.ScrolledText(results_frame, width=100, height=20, wrap=tk.WORD)
        self.advanced_results.pack(fill=tk.BOTH, expand=True)
    
    def _create_status_bar(self):
        """Create status bar."""
        self.status_bar = ttk.Label(self.root, text="Ready", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def update_status(self, message):
        """Update status bar message."""
        self.status_bar.config(text=message)
        self.root.update_idletasks()
    
    # Book operations
    def add_book(self):
        """Add a new book to the library."""
        try:
            title = self.book_title_var.get().strip()
            author = self.book_author_var.get().strip()
            isbn = self.book_isbn_var.get().strip()
            year = int(self.book_year_var.get())
            book_type = self.book_type_var.get()
            
            if not all([title, author, isbn]):
                messagebox.showwarning("Input Error", "Please fill in all required fields")
                return
            
            # YK: added isbn validation before inserting
            valid_isbn = utils.validate_isbn(isbn)
            if not valid_isbn:
                messagebox.showwarning("Input Error", f"Invalid isbn {isbn}")
                return

            book = None
            if book_type == "Physical":
                shelf = self.shelf_var.get()
                condition = self.condition_var.get()
                book = PhysicalBook(title, author, isbn, year, shelf, condition)
            elif book_type == "EBook":
                filesize = float(self.filesize_var.get())
                format_type = self.format_var.get()
                book = EBook(title, author, isbn, year, filesize, format_type)
            elif book_type == "AudioBook":
                narrator = self.narrator_var.get()
                duration = int(self.duration_var.get())
                book = AudioBook(title, author, isbn, year, narrator, duration)
            
            # YK: added pub_year validation before inserting
            book.publication_year = year
            if not book.publication_year:
                messagebox.showwarning("Input Error", f"Invalid publication year {year}")
                return
            
            self.library.add_book(book)
            self.refresh_books()
            self.update_status(f"Added book: {title}")
            messagebox.showinfo("Success", f"Book '{title}' added successfully!")
            
            # Clear fields
            self.book_title_var.set("")
            self.book_author_var.set("")
            self.book_isbn_var.set("")
            self.book_year_var.set("")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add book: {str(e)}")
    
    def view_book_details(self):
        """View details of selected book."""
        selection = self.books_tree.selection()
        if not selection:
            messagebox.showwarning("Selection Error", "Please select a book")
            return
        
        item = self.books_tree.item(selection[0])
        isbn = str(item['values'][3])  # ISBN is at index 3; YK: added str() for isbn w/o dash becomes int!!!
        
        book = self.library.find_book(isbn)
        if book:
            details = f"Book Details\n{'='*39}\n\n"
            details += f"Title: {book.title}\n"
            details += f"Author: {book.author}\n"
            details += f"ISBN: {book.isbn}\n"
            details += f"Year: {book.publication_year}\n"
            details += f"Type: {book.get_type()}\n"
            details += f"Available: {'Yes' if book.available else 'No'}\n"
            
            if isinstance(book, PhysicalBook):
                details += f"Shelf: {book.shelf_location}\n"
                details += f"Condition: {book.condition}\n"
            elif isinstance(book, EBook):
                details += f"File Size: {book.file_size} MB\n"
                details += f"Format: {book.format}\n"
                details += f"Downloads: {book.download_count}\n"
            elif isinstance(book, AudioBook):
                details += f"Narrator: {book.narrator}\n"
                details += f"Duration: {book.duration_minutes} minutes\n"
                details += f"Plays: {book.play_count}\n"
            
            messagebox.showinfo("Book Details", details)
    
    # Member operations
    def add_member(self):
        """Add a new member to the library."""
        try:
            name = self.member_name_var.get().strip()
            member_id = self.member_id_var.get().strip()
            email = self.member_email_var.get().strip()
            member_type = self.member_type_var.get()
            
            if not all([name, member_id, email]):
                messagebox.showwarning("Input Error", "Please fill in all required fields")
                return
            
            # YK: added e-mail validation before inserting
            valid_email = utils.validate_email(email)
            if not valid_email:
                messagebox.showwarning("Input Error", f"Invalid e-mail {email}")
                return
            
            member = None
            if member_type == "Regular":
                member = Member(name, member_id, email)
            elif member_type == "Student":
                student_id = self.student_id_var.get()
                university = self.university_var.get()
                member = StudentMember(name, member_id, email, student_id, university)
            elif member_type == "Premium":
                expiry = self.expiry_var.get()
                member = PremiumMember(name, member_id, email, expiry)
            
            self.library.add_member(member)
            self.refresh_members()
            self.update_status(f"Added member: {name}")
            messagebox.showinfo("Success", f"Member '{name}' added successfully!")
            
            # Clear fields
            self.member_name_var.set("")
            self.member_id_var.set("")
            self.member_email_var.set("")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add member: {str(e)}")
    
    def generate_member_id(self):
        """Generate a unique member ID."""
        member_id = utils.generate_id("M")
        self.member_id_var.set(member_id)
        self.update_status(f"Generated ID: {member_id}")
    
    def view_member_details(self):
        """View details of selected member."""
        selection = self.members_tree.selection()
        if not selection:
            messagebox.showwarning("Selection Error", "Please select a member")
            return
        
        item = self.members_tree.item(selection[0])
        member_id = item['values'][1]  # Member ID is at index 1
        
        member = self.library.find_member(member_id)
        if member:
            details = f"Member Details\n{'='*39}\n\n"
            details += f"Name: {member.name}\n"
            details += f"Member ID: {member.member_id}\n"
            details += f"Email: {member.email}\n"
            details += f"Type: {member.__class__.__name__}\n"
            details += f"Borrowed Books: {member.get_borrowed_count()}/{member.max_books}\n"
            
            if isinstance(member, StudentMember):
                details += f"Student ID: {member.student_id}\n"
                details += f"University: {member.university}\n"
            elif isinstance(member, PremiumMember):
                details += f"Expiry: {member.membership_expiry}\n"
                details += f"Status: {'Active' if not member.is_expired() else 'Expired'}\n"
            
            messagebox.showinfo("Member Details", details)
    
    # Transaction operations
    def borrow_book(self):
        """Process a book borrow request."""
        try:
            import io
            import contextlib
            
            member_id = self.borrow_member_var.get().strip()
            isbn = self.borrow_isbn_var.get().strip()
            date = self.borrow_date_var.get().strip()
            
            if not all([member_id, isbn, date]):
                messagebox.showwarning("Input Error", "Please fill in all fields")
                return
            
            # Capture output
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                self.library.borrow_book(member_id, isbn, date)
            
            output = f.getvalue()
            
            if "Success" in output or "✓" in output:
                messagebox.showinfo("Success", output)
                self.refresh_all()
            else:
                messagebox.showwarning("Borrow Failed", output)
            
            self.update_status("Borrow operation completed")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to borrow book: {str(e)}")
    
    def return_book(self):
        """Process a book return."""
        try:
            import io
            import contextlib
            
            member_id = self.return_member_var.get().strip()
            isbn = self.return_isbn_var.get().strip()
            date = self.return_date_var.get().strip()
            
            if not all([member_id, isbn, date]):
                messagebox.showwarning("Input Error", "Please fill in all fields")
                return
            
            # Capture output
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                self.library.return_book(member_id, isbn, date)
            
            output = f.getvalue()
            
            if "Success" in output or "✓" in output:
                messagebox.showinfo("Success", output)
                self.refresh_all()
            else:
                messagebox.showwarning("Return Failed", output)
            
            self.update_status("Return operation completed")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to return book: {str(e)}")
    
    # Search operations
    def search_library(self):
        """Search for books and members."""
        search_term = self.search_var.get().strip()
        if not search_term:
            messagebox.showwarning("Input Error", "Please enter a search term")
            return
        
        self.search_results.delete(1.0, tk.END)
        self.search_results.insert(tk.END, f"Search Results for: '{search_term}'\n")
        self.search_results.insert(tk.END, "="*70 + "\n\n")
        
        # Search books
        book_results = []
        for book in self.library.books:
            if book.matches_search(search_term):
                book_results.append(book)
        
        self.search_results.insert(tk.END, f"Books Found: {len(book_results)}\n")
        self.search_results.insert(tk.END, "-"*70 + "\n")
        for book in book_results:
            self.search_results.insert(tk.END, f"✓ {book.title} by {book.author} ({book.get_type()})\n")
            self.search_results.insert(tk.END, f"  ISBN: {book.isbn}, Available: {book.available}\n\n")
        
        # Search members
        member_results = []
        for member in self.library.members:
            if member.matches_search(search_term):
                member_results.append(member)
        
        self.search_results.insert(tk.END, f"\nMembers Found: {len(member_results)}\n")
        self.search_results.insert(tk.END, "-"*70 + "\n")
        for member in member_results:
            self.search_results.insert(tk.END, f"✓ {member.name} ({member.__class__.__name__})\n")
            self.search_results.insert(tk.END, f"  ID: {member.member_id}, Email: {member.email}\n\n")
        
        self.update_status(f"Search completed: {len(book_results)} books, {len(member_results)} members found")
    
    # Advanced feature tests
    def test_iterator(self):
        """Test library iterator."""
        self.advanced_results.delete(1.0, tk.END)
        self.advanced_results.insert(tk.END, "Testing Library Iterator\n")
        self.advanced_results.insert(tk.END, "="*70 + "\n\n")
        
        for i, book in enumerate(self.library, 1):
            self.advanced_results.insert(tk.END, f"{i}. {book.title} ({book.get_type()})\n")
        
        self.update_status("Iterator test completed")
    
    def test_available_books(self):
        """Test available books generator."""
        self.advanced_results.delete(1.0, tk.END)
        self.advanced_results.insert(tk.END, "Available Books (Generator)\n")
        self.advanced_results.insert(tk.END, "="*70 + "\n\n")
        
        count = 0
        for book in self.library.available_books():
            count += 1
            self.advanced_results.insert(tk.END, f"✓ {book.title} by {book.author}\n")
        
        self.advanced_results.insert(tk.END, f"\nTotal available: {count}\n")
        self.update_status(f"Found {count} available books")
    
    def test_books_by_author(self):
        """Test books by author generator."""
        author = self.author_search_var.get().strip()
        if not author:
            messagebox.showwarning("Input Error", "Please enter an author name")
            return
        
        self.advanced_results.delete(1.0, tk.END)
        self.advanced_results.insert(tk.END, f"Books by '{author}' (Generator)\n")
        self.advanced_results.insert(tk.END, "="*70 + "\n\n")
        
        count = 0
        for book in self.library.books_by_author(author):
            count += 1
            self.advanced_results.insert(tk.END, f"✓ {book.title} ({book.publication_year})\n")
        
        if count == 0:
            self.advanced_results.insert(tk.END, "No books found for this author.\n")
        
        self.update_status(f"Found {count} books by {author}")
    
    def test_books_by_type(self):
        """Test books by type generator."""
        book_type = self.type_search_var.get()
        
        self.advanced_results.delete(1.0, tk.END)
        self.advanced_results.insert(tk.END, f"Books of type '{book_type}' (Generator)\n")
        self.advanced_results.insert(tk.END, "="*70 + "\n\n")
        
        count = 0
        for book in self.library.books_by_type(book_type):
            count += 1
            self.advanced_results.insert(tk.END, f"✓ {book.title} by {book.author}\n")
        
        if count == 0:
            self.advanced_results.insert(tk.END, "No books found of this type.\n")
        
        self.update_status(f"Found {count} books of type {book_type}")
    
    def test_active_members(self):
        """Test active members generator."""
        self.advanced_results.delete(1.0, tk.END)
        self.advanced_results.insert(tk.END, "Active Members (Generator)\n")
        self.advanced_results.insert(tk.END, "="*70 + "\n\n")
        
        count = 0
        for member in self.library.active_members():
            count += 1
            self.advanced_results.insert(tk.END, f"✓ {member.name} - Borrowed: {member.get_borrowed_count()}\n")
        
        if count == 0:
            self.advanced_results.insert(tk.END, "No active members found.\n")
        
        self.update_status(f"Found {count} active members")
    
    def test_email_validation(self):
        """Test email validation utility."""
        email = tk.simpledialog.askstring("Email Validation", "Enter email to validate:")
        if email:
            result = utils.validate_email(email)
            messagebox.showinfo("Validation Result", 
                              f"Email: {email}\nValid: {result}")
    
    def test_isbn_validation(self):
        """Test ISBN validation utility."""
        isbn = tk.simpledialog.askstring("ISBN Validation", "Enter ISBN to validate:")
        if isbn:
            result = utils.validate_isbn(isbn)
            messagebox.showinfo("Validation Result", 
                              f"ISBN: {isbn}\nValid: {result}")
    
    def test_date_calc(self):
        """Test date calculation utility."""
        date1 = tk.simpledialog.askstring("Date Calculation", "Enter first date (YYYY-MM-DD):")
        if date1:
            date2 = tk.simpledialog.askstring("Date Calculation", "Enter second date (YYYY-MM-DD):")
            if date2:
                days = utils.calculate_days_between(date1, date2)
                messagebox.showinfo("Calculation Result", 
                                  f"Days between {date1} and {date2}: {days}")
    
    # Refresh operations
    def refresh_books(self):
        """Refresh books display."""
        for item in self.books_tree.get_children():
            self.books_tree.delete(item)
        
        for i, book in enumerate(self.library.books, 1):
            available = "✓" if book.available else "✗"
            self.books_tree.insert("", tk.END, text=str(i), 
                                  values=(book.title, book.author, book.get_type(), 
                                         book.isbn, available))
        
        self.update_status(f"Books refreshed: {len(self.library.books)} total")
    
    def refresh_members(self):
        """Refresh members display."""
        for item in self.members_tree.get_children():
            self.members_tree.delete(item)
        
        for i, member in enumerate(self.library.members, 1):
            self.members_tree.insert("", tk.END, text=str(i), 
                                    values=(member.name, member.member_id, member.email,
                                           member.__class__.__name__, 
                                           member.get_borrowed_count(), member.max_books))
        
        self.update_status(f"Members refreshed: {len(self.library.members)} total")
    
    def refresh_transactions(self):
        """Refresh transactions display."""
        for item in self.trans_tree.get_children():
            self.trans_tree.delete(item)
        
        for i, trans in enumerate(self.library.transactions, 1):
            status = "✓ Returned" if trans.is_returned else "Active"
            return_date = trans.return_date if trans.return_date else "N/A"
            self.trans_tree.insert("", tk.END, text=str(i), 
                                  values=(trans.transaction_id, trans.member.name,
                                         trans.book.title, trans.borrow_date,
                                         return_date, status))
        
        self.update_status(f"Transactions refreshed: {len(self.library.transactions)} total")
    
    def refresh_all(self):
        """Refresh all displays."""
        self.refresh_books()
        self.refresh_members()
        self.refresh_transactions()
        self.update_status("All displays refreshed")
    
    def show_about(self):
        """Show about dialog."""
        about_text = """Library Management System - Interactive GUI
        
Version 1.0

A comprehensive testing interface for the OOP Final Assignment.

Features:
• Book Management (Physical, EBook, AudioBook)
• Member Management (Regular, Student, Premium)
• Transaction Processing (Borrow/Return)
• Search Functionality
• Iterator and Generator Testing
• Utility Function Testing

Built with Python and Tkinter
"""
        messagebox.showinfo("About", about_text)


def main():
    """Main entry point for the GUI application."""
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()


if __name__ == "__main__":
    # Add simple dialog support
    import tkinter.simpledialog
    main()
