# 0x01. AirBnB clone - Web static

### `HTML` `CSS` `Front-end`

### Background Context

#### Web static, what?

Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

- Create simple HTML static pages
- Style guide
- Fake contents
- No Javascript
- No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

## Resources

**Read or watch**:

- [Learn to Code HTML & CSS](https://learn.shayhowe.com/html-css/) (_until “Creating Lists” included_)
- [Inline Styles in HTML](https://www.codecademy.com/article/html-inline-styles)
- [Specifics on CSS Specificity](https://css-tricks.com/specifics-on-css-specificity/)
- [CSS SpeciFishity](http://www.standardista.com/cgi-sys/suspendedpage.cgi)
- [Introduction to HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
- [MDN](https://developer.mozilla.org/en-US/)
- [center boxes](https://css-tricks.com/centering-css-complete-guide/)

### General

- What is HTML
- How to create an HTML page
- What is a markup language
- What is the DOM
- What is an element / tag
- What is an attribute
- How does the browser load a webpage
- What is CSS
- How to add style to an element
- What is a class
- What is a selector
- How to compute CSS Specificity Value
- What are Box properties in CSS

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `W3C` compliant and validate with [W3C-Validator](https://github.com/holbertonschool/W3C-Validator)
- All your CSS files should be in `styles` folder
- All your images should be in `images` folder
- You are not allowed to use `!important` and `id` (`#...` in the CSS file)
- You are not allowed to use tags `img`, `embed` and `iframe`
- You are not allowed to use `Javascript`
- Current screenshots have been done on `Chrome 56` or more.
- No cross browsers
- You have to follow all requirements but some `margin`/`padding` are missing - you should try to fit as much as you can to screenshots

## More Info

![hbnb_step1](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/e9017383-629b-4764-b0b6-7a8d010ae501)

## Tasks

[0. Inline styling](./0-index.html)

Write an HTML page that displays a header and a footer.

Layout:

- Body:
  - no margin
  - no padding
- Header:
  - color `#FF0000` (red)
  - height: `70px`
  - width: `100%`
- Footer:
  - color `#00FF00` (green)
  - height: `60px`
  - width: `100%`
  - text `Best School` center vertically and horizontally
  - always at the bottom at the page

**Requirements**:

- You must use the `header` and `footer` tags
- You are not allowed to import any files
- You are not allowed to use the `style` tag in the `head` tag
- Use inline styling for all your tags

![Screenshot from 2023-05-21 15-54-23](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/8898eb46-0704-48a2-9d6b-b442084f55f8)

[1. Head styling](./1-index.html)

Write an HTML page that displays a `header` and a `footer` by using the `style` tag in the `head` tag (same as `0-index.html`)

**Requirements**:

- You must use the `header` and `footer` tags
- You are not allowed to import any files
- No inline styling
- You must use the `style` tag in the `head` tag

The layout must be exactly the same as [0-index.html](./0-index.html)

![Screenshot from 2023-05-21 15-54-37](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/136ae61c-9e4d-44ff-9f7c-80930c9b9af2)

[2. CSS files](./2-index.html)

Write an HTML page that displays a `header` and a `footer` by using CSS files (same as `1-index.html`)

**Requirements**:

- You must use the `header` and `footer` tags
- No inline styling
- You must have `3` CSS files:
  * [styles/2-common.css](./styles/2-common.css): for `global` style (*i.e._ the `body` style)
  _ [styles/2-header.css](./styles/2-header.css): for `header` style \* [styles/2-footer.css](./styles/2-footer.css): for `footer` style
  The layout must be exactly the same as `1-index.html`

![Screenshot from 2023-05-21 15-54-54](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/b06103f2-3ecb-401a-bc0b-ca2f4a1fbcb3)

[3. Zoning done!](./3-index.html)

Write an HTML page that displays a header and footer by using CSS files (same as `2-index.html`)

**Layout**:

- Common:
  - no margin
  - no padding
  - font color: `#484848`
  - font size: `14px`
  - font family: `Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;`
  - [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon.png) in the browser tab
- Header:
  - color: `white`
  - height: `70px`
  - width: `100%`
  - border bottom `1px #CCCCCC`
  - [logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/logo.png) align on `left` and `center` vertically (`20px` space at the left)
- Footer:
  - color `white`
  - height: `60px`
  - width: `100%`
  - border top `1px #CCCCCC`
  - text `Best School` center vertically and horizontally
  - always at the `bottom` at the page

**Requirements**:

- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have `3` CSS files:
- `styles/3-common.css`: for the global style (i.e `body` style)
- `styles/3-header.css`: for the `header` style
- `styles/3-footer.css`: for the `footer` style

![Screenshot from 2023-05-21 15-55-09](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/fb57cb66-b035-420f-ba8f-3102b7c7ade7)

[4. Search!](./4-index.html)

Write an HTML page that displays a `header`, `footer` and a `filters` box with a `search` button.

**Layout**: (based on [3-index.html](./3-index.html))

- Container:
  - between `header` and `footer` tags, add a `div`:
  - classname: `container`
  - max width `1000px`
  - margin `top` and `bottom` `30px` - it should be `30px` under the bottom of the header (screenshot)
  - center horizontally
- Filter section:
  - tag `section`
  - classname `filters`
  - inside the `.container`
  - color `white`
  - height: `70px`
  - width: `100%` of the container
  - border `1px #DDDDDD` with radius `4px`
- Button search:
  - tag `button`
  - text `Search`
  - font size: `18px`
  - inside the section `filters`
  - background color `#FF5A5F`
  - text color `#FFFFFF`
  - height: `48px`
  - width: `20%` of the section filters
  - no borders
  - border radius: `4px`
  - center vertically and at `30px` of the right border
  - change opacity to `90%` when the mouse is on the button

**Requirements**:

- You must use: `header`, `footer`, `section`, `button` tags
- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the` images` folder
- You must have `4` CSS files:
- `styles/4-common.css`: for the global style (`body` and `.container` styles)
- `styles/3-header.css`: for the `header` style
- `styles/3-footer.css`: for the `footer` style
- `styles/4-filters.css`: for the `filters` style
- `4-index.html` **won’t be W3C valid**, don’t worry, it’s temporary

![Screenshot from 2023-05-21 15-55-46](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/2d9686b8-1431-4022-8ab8-b9cec110de37)

[5. More filters](./5-index.html)

Write an HTML page that displays a `header`, `footer` and a `filters` box.

Layout: (based on `4-index.html`)

- Locations and Amenities filters:
  - tag: `div`
  - classname: `locations` for `location` tag and `amenities` for the other
  - inside the section filters (same level as the button Search)
  - height: `100%` of the section filters
  - width: `25%` of the section filters
  - border right `#DDDDDD 1px` only for the first `left` filter
  - contains a title:
    - tag: `h3`
    - font weight: `600`
    - text `States` or `Amenities`
  - contains a subtitle:
    - tag: `h4`
    - font weight: `400`
    - font size: `14px`
    - text with fake contents

**Requirements**:

- You must use: `header`, `footer`, `section`, `button`, `h3`, `h4` tags
- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have `4` CSS files:
  - `styles/4-common.css`: for the global style (`body` and `.container` styles)
  - `styles/3-header.css`: for the `header` style
  - `styles/3-footer.css`: for the `footer` style
  - `styles/5-filters.css`: for the `filters` style

![Screenshot from 2023-05-21 15-55-58](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/dd843686-f471-4d35-9579-d6a57568c375)

[6. It's (h)over](./6-index.html)

Write an HTML page that displays a `header`, `footer` and a `filters` box with `dropdown`.

Layout: (based on [5-index.html](./5-index.html))

- Update `Locations` and `Amenities` filters to display a contextual dropdown when the mouse is on the filter `div`:
  - tag `ul`
  - classname `popover`
  - text should be fake now
  - inside each `div`
  - not displayed by default
  - color `#FAFAFA`
  - `width` same as the `div` filter
  - border `#DDDDDD 1px` with border radius `4px`
  - no list display
  - Location filter has `2` levels of `ul/li`:
    - `state -> cities`
    - state name must be display in a `h2` tag (font size `16px`)

**Requirements**:

- You must use: `header`, `footer`, `section`, `button`, `h3`, `h4`, `ul`, `li` tags
- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have `4` CSS files:
  - `styles/4-common.css`: for the global style (`body` and `.container` styles)
  - `styles/3-header.css`: for the `header` style
  - `styles/3-footer.css`: for the `footer` style
  - `styles/6-filters.css`: for the `filters` style

![Screenshot from 2023-05-21 15-56-15](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/26d5d776-821a-47ff-b351-33d6d48c6829)

![Screenshot from 2023-05-21 15-56-19](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/f94cad12-9075-4832-be18-697b90a69af3)

[7. Display results](./7-index.html)

Write an HTML page that displays a `header`, `footer`, a `filters` box with `dropdown` and `results`.

Layout: (based on [6-index.html](./6-index.html))

- Add Places section:
  _ tag: `section`
  _ classname: `places`
  _ same level as the filters section, inside `.container`
  _ contains a title:
  _ tag: `h1`
  _ text: `Places`
  _ align in the `top left`
  _ font size: `30px`
  _ contains multiple “Places” as listing (horizontal or vertical) describe by:
  _ tag: `article`
  _ width: `390px`
  _ padding and margin `20px`
  _ border `#FF5A5F 1px` with radius `4px`
  _ contains the place name:
  _ tag: `h2`
  _ font size: `30px` \* center horizontally
  **Requirements**:

- You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2`, `h3`, `h4`, `ul`, `li` tags
- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have `5` CSS files:
  - `styles/4-common.css`: for the global style (i.e. `body` and `.container` styles)
  - `styles/3-header.css`: for the `header` style
  - `styles/3-footer.css`: for `footer` style
  - `styles/6-filters.css`: for the `filters` style
  - `styles/7-places.css`: for the `places` style

![Screenshot from 2023-05-21 15-56-34](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/8f633d55-217a-4ca6-b05e-85e71399c839)

[8. More details](./8-index.html)

Write an HTML page that displays a `header`, a `footer`, a `filter` box (_dropdown list_) and the result of the `search`.

Layout: (based on [7-index.html](./7-index.html))

Add more information to a `Place` article:

- Price by night:
  - tag: `div`
  - classname: `price_by_night`
  - same level as the place name
  - font color: `#FF5A5F`
  - border: `#FF5A5F 4px` rounded
  - min width: `60px`
  - height: `60px`
  - font size: `30px`
  - align: the top right (with space)
- Information section:
  - tag: `div`
  - classname: `information`
  - height: `80px`
  - border: top and bottom `#DDDDDD 1px`
  - contains (align vertically):
    - Number of guests:
      - tag: `div`
      - classname: `max_guest`
      - width: `100px`
      - fake text
      - icon
    - Number of bedrooms:
      - tag: `div`
      - classname: `number_rooms`
      - width: `100px`
      - fake text
      - icon
    - Number of bathrooms:
      - tag: `div`
      - classname: `number_bathrooms`
      - width: `100px`
      - fake text
      - icon
- User section:
  - tag: `div`
  - classname: `user`
  - text Owner: `<fake text>`
  - Owner text should be in bold
- Description section:
  - tag: `div`
  - classname: `description`

**Requirements**:

- You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2`, `h3`, `h4`, `ul`, `li` tags
- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have 5 CSS files:
  - `styles/4-common.css`: for the global style (i.e. `body` and `.container` styles)
  - `styles/3-header.css`: for the `header` style
  - `styles/3-footer.css`: for the `foote`r style
  - `styles/6-filters.css`: for the `filters` style
  - `styles/8-places.css`: for the `places` style

![Screenshot from 2023-05-24 23-00-51](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/1c75a333-4c66-4df6-8671-9b4d48a42155)

[9. Full details](./100-index.html)

Write an HTML page that displays a `header`, `footer`, a `filters` box with dropdown and results.

Layout: (based on [8-index.html](./8-index.html))

Add more information to a Place `article`:

- List of Amenities:
  - tag `div`
  - classname `amenities`
  - margin top `40px`
  - contains:
    - title:
      - tag `h2`
      - text `Amenities`
      - font size `16px`
      - border bottom `#DDDDDD 1px`
    - list of amenities:
      - tag `ul` / `li`
      - no list style
      - icons on the left: [Pet friendly](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_pets.png), [TV](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_tv.png), [Wifi](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_wifi.png), etc… feel free to add more
- List of Reviews:
  - tag `div`
  - classname `reviews`
  - margin top `40px`
  - contains:
    - title:
      - tag `h2`
      - text `Reviews`
      - font `size 16px`
      - border bottom `#DDDDDD 1px`
    - list of review:
      - tag `ul` / `li`
      - no list style
      - a review is described by:
        - `h3` tag for the `user/date` description (font size `14px`). Ex: “From Bob Dylan the 27th January 2017”
        - `p` tag for the text (font size `12px`)

**Requirements**:

- You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2`, `h3`, `h4`, `ul`, `li` tags
- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have `5` CSS files:
  - `styles/4-common.css`: for the global style (`body` and `.container` styles)
  - `styles/3-header.css`: for the `header` style
  - `styles/3-footer.css`: for the `footer` style
  - `styles/6-filters.css`: for the `filters` style
  - `styles/100-places.css`: for the `places` style

![Screenshot from 2023-05-24 23-01-43](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/b17e946f-3fc3-49d8-8348-4e1c0d2b3692)

[10. Flex](./101-index.html)

Improve the Places section by using [Flexible boxes](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) for all Place articles

[Flexbox Froggy](http://flexboxfroggy.com/)

https://www.loom.com/share/1ced4804eea74de39df0a23e3d1929b9

[11. Responsive design](./102-index.html)

Improve the page by adding [responsive design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design) to display correctly in mobile or small screens.

**Examples**:

- no horizontal scrolling
- redesign search bar depending of the `width`
- etc.

https://www.loom.com/share/cd4900d7ae40404781a09692ddbe710f

[12. Accessibility](./103-index.html)

Improve the page by adding [Accessibility support](https://developer.mozilla.org/en-US/docs/Learn/Accessibility)

**Examples**:

- Colors contrast
- Header tags
- etc.

![Screenshot from 2023-05-22 07-24-25](https://github.com/samuelselasi/AirBnB_clone/assets/85158665/9a791be7-9533-4f7d-8008-66d449da42ee)
