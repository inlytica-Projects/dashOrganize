# dashOrganize
Example of how to organize large Dash project by tab.

```
.
├── app.py                   
├── assets                   
├── components.py
├── index.py
├── tabs
├── tallAnimals.csv
└── usefulFunctions.py
```
app.py
Only role is to supply the Dash instance to other modules. If you try to include the ```app = Dash(__name__, suppress_callback_exceptions=True)``` line in index.py and then import it, you will get 'ImportError: cannot import name ...' . This is because you have created a circular import. In this case, for example, loading index.py requires animalsFeet.py while, at the same time, animalsFeet.py requires the Dash instance from index.py. It would be a little like Bob needing a key from Susan to start his car and Susan needing Bob's car to bring him the key.

assets
Directory containing formatting files. In this case, I am using the bootstrap CSS Darkly Theme from Bootswatch (https://bootswatch.com) who, by the way, offer these amazing designs for free.

components.py
A library of Dash components. I've gone back and forth on the idea of a components file because, at times, it seems as if I am re-creating the Plotly wheel. I finally settled on using it because it helps keep keep formatting consistent across all of my components. It reduces the need to clutter up my layouts with formatting elements. And, because I work with multiple clients, once I get components formatted in the way that I am happy with, I can easilty reuse them. (This file is for example purposes. My actual working file is so large that I have thought about breaking it down even more.)

index.py
Basically just gathers the layouts from other files and deploys the application.

tabs
Holds the files that actually do something. Each file under the tabs directory returns a complete layout for that tab with components imported from the components.py file. My callbacks return Div's because, for charts, I have to return a dcc.Graph component. So, while I could use a callback to return the "figure" part of it, I cannot seem to incorporate formatting (fig.update_layout, etc.) without adding it to each and every callback - which pretty much defeats the purpose of a components file. I return all of the other components (like Dropdown) in a Div for consistency and because, frankly, I think the code looks cleaner with one callback output vs one for every element of a component.    

usefulFunctions.py
Provides functions that I use over and over. While this example is trivial, my actual file would contain functions that upload / download data to a Redis cache, convert strings to dates, provide button functionality, etc. etc.  

