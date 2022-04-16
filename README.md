# Integration of htmx Made Easy

The main goal of this repo is to give detailed guidelines for projects aiming to
use htmx, but have an existing code source that is not easy to migrate in a short
amount of time.

Another goal is to prove for not-so-convinced people by htmx that it is very easy
to integrate in almost any project, with a very minimal amount of effort.

In this README, we are taking about generic aspects that can be adapted to any
framework.  
But you will also find sample projects for several well-know frameworks.  

Actually available:

- [Django](https://github.com/yahya-abou-imran/htmx-gradual-adoption/tree/main/django)

## The Problem to Resolve

Your HTTP responses are returning full HTML pages content… but you just want a
part of the page to be updated.  
If we begin to use htmx without thinking, we are going to put an entire big page
inside little poor buttons (which is horrible and unfair…).  

We don’t want to change or backend right of the bat, we want a solution to begin
using htmx step by step, without big architectural changes touching the entire
web app…

What can we do?

## The Solution

**Use [`hx-select`](https://htmx.org/attributes/hx-select/)**

It takes a CSS selector, and will just take the matching element(s) from the
response page to update the target.

Most of the time, you will just have to give it the same value as `hx-target`,
And all we be fine perfectly fine!

If you have good IDs, or HTML tags than can be found without ambiguity (i.e.
`hx-target="closest tr"`), you don’t need to change anything in your HTML templates.  
If it’s not the case, just try to put well-chosen IDs to the elements which are
to be swapped by an htmx request.

### Simple Example

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


#### Full migration solution

If you want to switch to htmx completely, the steps are very simple:
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


#### Accessibility, Progressive Enhancement

If you want to support browsers where JS is not enable, or you want to let
screen readers use natural attributes, you can let the original attributes
alongside the htmx ones:

```html
<a href="/elsewhere"
   hx-get="/elsewhere"
   hx-target="#content-detail"
   hx-select="#content-detail">
  See Other!
</a>

<form method="post"
      action="/process"
      hx-post="/process"
      hx-target=".content-wrapper"
      hx-select=".content-wrapper">
  <button>Let’s do it!</button>
</form>
```

But it means that you have to handle in the backend end both standards requests
and htmx ones…  
This is the goal of the next section.

#### Refactoring the backend

Of course, there is a performance issue, because, in the backend side, we are
building the full HTML content for each request.  
We want now to only render the fragment of the template that is the one we want
to render.  
If we can do that, we can drop the `hx-select` that becomes of course superfluous.

In another hand, we may have a handful cases where we always want to make a real
HTTP redirection and render a full page for some reasons (like in the previous section).  
So, if we could tell in advance if the request has been done through htmx or not,
it will be more easy to handle the two cases in our backend.

Hopefully, htmx sets a header called `HX-Request` (or `hx-request`) at `true` for
each request done from it. Now we can tell we want have to do!

The algorithm is very simple:

- If htmx request:
    - perform backend operations
    - render and return the template fragment
- Else:
    - process it like usual

If your framework is using an MVC pattern (or a derivative of it), and is 
representing controllers with classes, you can easily write some kind of mixin
(base class, interfaces…) of the sort (python-like pseudocode):

```python
class HtmxMixin:

    template: str = ""
    template_fragment: str = ""

    def is_htmx_request(self) -> bool:
        if self.request.get_header("HX-Request") == "true":
            return True
        else:
            return False

    def process_request(self):
        if not self.is_htmx_request():
            # this should do a `self.render(self.template)`
            return super().process_request()
        else:
            self.process_htmx_request()
            return self.render(self.template_fragment)

    @abstract
    def process_htmx_request(self):
        ...
```

Of course, `process_request` and `render` are only examples, and you have to 
adapt it to your framework.
