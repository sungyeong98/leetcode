select u.name, t.balance
from (
    select account, sum(amount) as balance
    from Transactions
    group by account
) t
inner join Users u on
    t.account=u.account
where t.balance>10000