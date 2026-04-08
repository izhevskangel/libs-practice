# import matplotlib.pyplot as plt
# import seaborn as sns
#
# # 1. Знаходимо ТОП-5 країн за рівнем депресії
# top_5_depression = df.nlargest(5, 'depression_score')
#
# # 2. Будуємо графік
# plt.figure(figsize=(10, 6))
#
# # Малюємо лінію для депресії
# sns.lineplot(data=top_5_depression, x='country', y='depression_score',
#              marker='o', label='Депресія', color='royalblue')
#
# # Малюємо лінію для тривожності на тому самому полотні
# sns.lineplot(data=top_5_depression, x='country', y='anxiety_score',
#              marker='s', label='Тривожність', color='orange')
#
# plt.title('Порівняння рівнів депресії та тривожності (ТОП-5 країн)')
# plt.xlabel('Країна')
# plt.ylabel('Показник')
# plt.legend()
# plt.grid(True, linestyle='--', alpha=0.6)
# plt.show()
#
#
#
#
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# # Налаштовуємо стиль
# sns.set_theme(style="whitegrid")
#
# plt.figure(figsize=(10, 6))
#
# sns.scatterplot(data=df,
#                 x='social_media_hours_daily',
#                 y='youth_mh_crisis_score',
#                 alpha=0.6,
#                 color='teal')
#
# plt.title('Зв’язок часу в соцмережах та ментального здоров’я молоді')
# plt.xlabel('Годин у соцмережах щодня')
# plt.ylabel('Індекс ментальної кризи (Youth MH Crisis Score)')
#
# plt.show()



plt.figure(figsize=(8,4))
