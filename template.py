# pandas 
pd.set_option('display.max_rows', None)      # display max rows  

###########################################################
# subplots-1    2 adjacent plots
fig, axs = plt.subplots(2, 1)
fig.suptitle("suptitle")
axs[0].plot(df['x'],df['y'])
axs[0].title.set_text('AAAAAAAAAAAAAAAAAAAAAAA')
axs[1].plot(df['x'],df['y'])
axs[1].title.set_text('BBBBBBBBBBBBB')


# subplots-2    2*2 = 4 plots
fig, axs = plt.subplots(2, 2)
axs[0,0].plot(df['x'],df['y'])
axs[0,0].ticklabel_format(useOffset=False, style='plain')   # to remove scientific notation
axs[0,1].plot(df['x'],df['y'])
axs[1,0].plot(df['x'],df['y'])
axs[1,1].plot(df['x'],df['y'])
###########################################################
