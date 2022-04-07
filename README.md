# Integration of htmx made easy

## The problem

Your HTTP responses return full HTML pages… But you just want a part of the page
to be updated.

## The solution
Use `hx-select`, and give it the same value as `hx-target`

Most of the time, you will have t
If you have good IDs, our HTML tags than can be found without ambiguity, you don’t
need to change anything in your HTML templates.  
If it’s not the case, just try to put well-chosen IDs to the elements which you
want to replace by an htmx request.

### The solution

Here are the two simple elements:

```html
<a href="/elsewhere">
  See Other!
</a>

<form method="post" action="/process">
  <button>Let’s do it!</button>
</form>
```

Let’s say that the `/elsewhere` redirect us to a similar page with another
content at the center of the page.  
As for `/process` it may just change something in the database related to the
current content, then redirect to the current with details updated.

The steps are very simple:
1. Include the htmx CDN
2. Use htmx to perform the GET and the POST:
    - Replace `href` by `hx-get` 
    - Replace `action` by `hx-post` and remove the `method="post"`
3. Use `hx-target` and `hx-select` to the same value


```html
<a hx-get="/elsewhere"
   hx-target="#content-detail"
   hx-select="#content-detail">
  See Other!
</a>

<form hx-post="/process"
      hx-target=".content-wrapper"
      hx-select=".content-wrapper">
  <button>Let’s do it!</button>
</form>
```
