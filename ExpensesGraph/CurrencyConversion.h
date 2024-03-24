#ifndef CURRENCY_CONVERSION_H
#define CURRENCY_CONVERSION_H
#include "../ParserExpenses/ParserExpenses.h"
#include "../ParserAccounts/ParserAccounts.h"

#define MAX_ACCOUNTS 10
#define MAX_USERS 50


typedef struct {
    double totalExpenseInSGD;
} ExpenseTotalsSGD;


void calculateExpenseTotal(Expenses *expenses, int numExpenses);
void printAllExpenseTotals(Expenses *expenses, int numExpenses, Account *accounts, int numAccounts);
void printExpenseTotal(int accountId, double totalExpenseInSGD);


#endif /* CURRENCY_CONVERSION_H */

