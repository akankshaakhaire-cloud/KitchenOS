# KitchenOS

# 1. User Roles Overview

KitchenOS follows a Role-Based Access Control (RBAC) model. Each user is assigned one or more roles, and every role has predefined permissions that determine what actions can be performed within the system.

This approach improves security, simplifies permission management, and ensures users only access the features required for their responsibilities.

---

# 2. Role Hierarchy

```text
Super Admin
      │
Restaurant Owner
      │
Branch Manager
      │
──────────────────────────────
│            │              │
Cashier   Inventory Manager  Chef
│            │              │
Waiter   Kitchen Staff   Staff Member
```

---

# 3. Available Roles

## Super Admin

Responsibilities:

- Manage all restaurants
- Manage subscriptions
- Manage system settings
- View all reports
- Manage all users
- Monitor application health

---

## Restaurant Owner

Responsibilities:

- Manage restaurant profile
- Manage branches
- Manage employees
- View reports
- Manage menu
- Manage inventory
- View financial reports

---

## Branch Manager

Responsibilities:

- Manage branch operations
- Approve inventory requests
- Manage staff
- View branch reports
- Manage daily operations

---

## Cashier

Responsibilities:

- Create orders
- Generate invoices
- Accept payments
- Print receipts
- Process refunds (if permitted)

---

## Chef

Responsibilities:

- View kitchen orders
- Update cooking status
- Mark food as ready
- Monitor kitchen queue

---

## Waiter

Responsibilities:

- Create table orders
- Serve customers
- Update order status
- View assigned tables

---

## Inventory Manager

Responsibilities:

- Manage stock
- Update inventory
- Create purchase orders
- Manage suppliers
- Monitor low stock

---

## Staff Member

Responsibilities:

- View assigned tasks
- Update task status
- Access personal profile

---

# 4. Permission Types

KitchenOS permissions follow CRUD operations.

- Create
- Read
- Update
- Delete

Additional permissions include:

- Approve
- Export
- Print
- Assign
- Manage
- Configure

---

# 5. Module Access Matrix

| Module | Super Admin | Owner | Manager | Cashier | Chef | Waiter | Inventory |
|---------|-------------|--------|----------|----------|-------|---------|------------|
| Dashboard | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Restaurant | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Branches | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Users | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Menu | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Inventory | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| Suppliers | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| Orders | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Kitchen | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| Reports | ✅ | ✅ | ✅ | Limited | ❌ | ❌ | Limited |
| Settings | ✅ | ✅ | Limited | ❌ | ❌ | ❌ | ❌ |

---

# 6. Authentication

All users authenticate using:

- Email
- Password
- JWT Access Token
- Refresh Token

Passwords are securely hashed using Bcrypt before storage.

---

# 7. Authorization

Authorization is enforced using RBAC.

Every protected API validates:

- Authentication
- Active Account
- Assigned Role
- Required Permission

Users without sufficient permissions receive:

- HTTP 401 Unauthorized
- HTTP 403 Forbidden

---

# 8. Security Rules

- Users access only their assigned restaurant.
- Branch users cannot access other branches.
- Soft-deleted users cannot log in.
- Disabled accounts cannot access APIs.
- Sensitive actions are recorded in Audit Logs.

---

# 9. Future Role Expansion

KitchenOS supports adding custom roles such as:

- Accountant
- Delivery Partner
- Marketing Manager
- HR Manager
- Regional Manager

without changing the existing architecture.

---

# 10. Conclusion

KitchenOS uses a flexible and scalable RBAC implementation to ensure secure access to application resources. The role hierarchy and permission model provide strong security while keeping the system easy to manage and extend as business requirements grow.