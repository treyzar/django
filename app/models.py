from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Category Name",
        help_text="Enter the category of the book (e.g., Fiction, Non-Fiction, Science, etc.)"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Category Slug",
        help_text="A URL-friendly version of the category name"
    )

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Publisher Name",
        help_text="Enter the name of the publisher"
    )
    website = models.URLField(
        max_length=255,
        blank=True,
        verbose_name="Publisher Website",
        help_text="Enter the website of the publisher"
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Book Title",
        help_text="Enter the title of the book"
    )
    author = models.CharField(
        max_length=255,
        verbose_name="Author",
        help_text="Enter the name of the author"
    )
    publication_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Publication Date",
        help_text="Format: YYYY-MM-DD"
    )
    desc = models.TextField(
        max_length=500,
        blank=True,
        verbose_name="Description",
        help_text="Enter a brief description of the book"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Category",
        help_text="Select the category of the book"
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Publisher",
        help_text="Select the publisher of the book"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price",
        help_text="Enter the price of the book"
    )
    cover_image = models.ImageField(
        upload_to='book_covers/',
        null=True,
        blank=True,
        verbose_name="Cover Image",
        help_text="Upload a cover image for the book"
    )
    isbn = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="ISBN",
        help_text="Enter the ISBN of the book (13 characters)"
    )


    def __str__(self):
        return self.title

    def full_name(self):
        return f"{self.title} - {self.author}"


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name="Book",
        help_text="Select the book for this review"
    )
    reviewer_name = models.CharField(
        max_length=255,
        verbose_name="Reviewer Name",
        help_text="Enter the name of the reviewer"
    )
    review_text = models.TextField(
        verbose_name="Review Text",
        help_text="Enter your review of the book"
    )
    rating = models.PositiveIntegerField(
        default=5,
        verbose_name="Rating",
        help_text="Enter a rating between 1 and 5"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the review was created"
    )

    def __str__(self):
        return f"Review by {self.reviewer_name} for {self.book.title}"