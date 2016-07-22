# coding=utf-8
__author__ = 'Dragan Vidakovic'
import xlsxwriter


def write_reviews(file, reviews):
    # prepare table
    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet()

    # prepare columns
    worksheet.set_column('A:A', 40)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 40)
    worksheet.set_column('E:E', 30)
    worksheet.set_column('F:F', 100)
    worksheet.set_column('G:G', 10)
    worksheet.set_column('H:H', 15)
    worksheet.set_column('I:I', 10)
    worksheet.set_column('J:J', 10)
    worksheet.set_column('K:K', 10)
    worksheet.set_column('L:L', 10)
    worksheet.set_column('M:M', 40)

    # enable bold header
    bold = workbook.add_format({'bold': True})

    # write header
    worksheet.write(0, 0, 'Restaurant URL', bold)
    worksheet.write(0, 1, 'Restaurant ', bold)
    worksheet.write(0, 2, 'User', bold)
    worksheet.write(0, 3, 'User URL', bold)
    worksheet.write(0, 4, 'Title', bold)
    worksheet.write(0, 5, 'Content', bold)
    worksheet.write(0, 6, 'Rating', bold)
    worksheet.write(0, 7, 'Published', bold)
    worksheet.write(0, 8, 'Food Quality', bold)
    worksheet.write(0, 9, 'Food Choice', bold)
    worksheet.write(0, 10, 'Prices', bold)
    worksheet.write(0, 11, 'Service', bold)
    worksheet.write(0, 12, 'Review URL', bold)

    # write content
    idx = 0
    while idx < len(reviews):
        review = reviews[idx]
        worksheet.write(idx+1, 0, review.restaurant_url)
        worksheet.write(idx+1, 1, review.restaurant_name)
        worksheet.write(idx+1, 2, review.username)
        worksheet.write(idx+1, 3, review.user_url)
        worksheet.write(idx+1, 4, review.title)
        worksheet.write(idx+1, 5, review.content)
        worksheet.write(idx+1, 6, review.rating)
        worksheet.write(idx+1, 7, review.published)
        worksheet.write(idx+1, 8, review.food_quality)
        worksheet.write(idx+1, 9, review.food_choice)
        worksheet.write(idx+1, 10, review.prices)
        worksheet.write(idx+1, 11, review.service)
        worksheet.write(idx+1, 12, review.url)
        idx += 1

    workbook.close()